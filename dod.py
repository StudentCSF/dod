class Character:

	def __init__(self) -> None:
		self.hp = 100
		self.energy = 100
		self.armor = 100
		self.ice_resistance = 0
		self.elictricity_resistance = 0
		self.fire_resistance = 0
		self.poison_resistance = 0
	
	def __str__(self) -> str:
		return f'Character(hp={self.hp}, energy={self.energy}, armor={self.armor}, ice_r={self.ice_resistance}, el_r={self.elictricity_resistance}, f_r={self.fire_resistance}, p_r={self.poison_resistance})'


class Charge:

	def __init__(self) -> None:
		self.physical_damage = 5
		self.fire_damage = 0
		self.electricity_damage = 0
		self.ice_damage = 0
		self.poison_damage = 0
		self.energy_cost = 5
	
	def __str__(self) -> str:
		return f'Charge(ph_dmg={self.physical_damage}, f_dmg={self.fire_damage}, el_dmg={self.electricity_damage}, ice_dmg={self.ice_damage}, pois_dmg={self.poison_damage}, cost={self.energy_cost})'


class Weapon:

	def __init__(self) -> None:
		self.physical_damage_modifier = 1
		self.money_cost = 30
	
	def __str__(self) -> str:
		return f'Weapon(mod={self.physical_damage_modifier}, cost={self.money_cost})'


weapon_charge_dict: dict[Weapon, Charge] = dict()
weapon_charge_dict[Weapon()] = Charge()
for k, v in weapon_charge_dict.items():
	print(k, v)
