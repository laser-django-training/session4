import random

class Lotto:
	winning_list = []
	users = []

	def __init__(self, balls_per_draw, total_balls, prizes):
		self.balls_per_draw = balls_per_draw
		self.total_balls = total_balls
		self.prizes = prizes

	def generate_winning(self):
		Lotto.winning_list.clear()
		for i in range(self.balls_per_draw):
			Lotto.winning_list.append(random.randint(1, self.total_balls))

	def read_user_balls(self, list_balls):
		self.users.append(list_balls)
		# users = [[1,2,3,4,5,6], [12,3,34,13,10,8]]

	def determine_winnings(self):
		winnings = []
		for user in self.users:
			result = 0
			for i in Lotto.winning_list:
				if i in user:
					result += 1
			if result > self.balls_per_draw - len(self.prizes):
				winnings.append(self.prizes[self.balls_per_draw - result + 1])
			else:
				winnings.append(0)
		return winnings

lotto = Lotto(6, 10, {1: 1000000, 2: 500000, 3: 250000})
lotto.generate_winning()
user_str = input("Enter 6 unique numbers between 1 and 52: ")
user_list = [int(x) for x in user_str.split(" ")]
lotto.read_user_balls(user_list)
win = lotto.determine_winnings()
print("Player has won {}$.".format(win[0]))
