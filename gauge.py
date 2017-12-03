import os

W1_DIR = '/sys/bus/w1/devices'
MASTER_DEVICE = 'w1_bus_master1'


def get_device():
	all_devices = os.listdir(W1_DIR)
	devices_except_master = set(all_devices) - set([MASTER_DEVICE])
	assert len(devices_except_master) == 1, "Expected just one 1w device; got: {}".format(devices_except_master)
	return list(devices_except_master)[0]


def temperature():
	with open(os.path.join(W1_DIR, get_device(), 'w1_slave')) as device:
		raw_text = device.read()
	
	t_equals = raw_text.strip().split(' ')[-1]
	temp_int = int(t_equals.split('=')[-1])
	
	temp_degrees = (1.0 * temp_int) / 1000
	return temp_degrees


if __name__ == '__main__':
	print(temperature())
