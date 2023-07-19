

class Data:
	def __init__(self, **kwargs) -> None:
		for key, value in kwargs.items():
			setattr(self, key, value)
   
	def to_dict(self) -> dict:
		data = {}
		for key, value in self.__dict__:
			if isinstance(self, getattr(self, value)):
				value = value.to_dict()
			data[key] = value
		return data
	
	@classmethod
	def from_dict(cls, data):
		kwargs = {}
		for key, value in data.items():
			if isinstance(value, dict):
				value = cls.from_dict(value)
			kwargs[key] = value
		return cls(**kwargs)
	
	def __setattr__(self, key, value) -> None:
		self.__dict__[key] = value
	
	def __getattr__(self, item):
		try:
			return self.__dict__[item]
		except KeyError:
			return AttributeError(f"{self.__class__.__name__} object has no attribute {item}")
	
	def __repr__(self) -> str:
		return f"{self.__class__.__name__}({self.__dict__})"



data = {
	"id": "1",
	"name": "first",
	"metadata": {
		"system": {
			"size": 10.7
		},
		"user": {
			"batch": 10
		}
	}
}
