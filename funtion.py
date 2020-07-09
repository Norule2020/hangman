from random import choice
def get_step(x_values,num_points):
	while(len(x_values)<num_points):
		x_direction=choice([-1,1])
		x_distance=choice([0,1,2,3])
		x_step=x_direction*x_distance
		y_direction=choice([-1,1])
		y_distance=choice([0,1,2,3])
		y_step=y_direction*y_distance
		#could not step on the same place
		if x_step==0 and y_step==0 :
			continue
