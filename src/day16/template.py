class FieldTemplate:

    def __init__(self):
        self.lower_min = 0
        self.lower_max = 0
        self.upper_min = 0
        self.upper_max = 0

    def validate(self, n):
        return (self.lower_min <= n <= self.lower_max) or (self.upper_min <= n <= self.upper_max)

    def validate_all(self, numbers):
        return all([self.validate(n) for n in numbers])


class FieldTemplates:

    def __init__(self):
        self.templates = {}

    def __setitem__(self, name, value):
        self.templates[name] = value

    def __getitem__(self, name):
        return self.templates[name]

    def __iter__(self):
        return self.templates.__iter__()

    def field_names(self):
        return list(self.templates.keys())

    def validate(self, n):
        for template in self.templates.values():
            if template.validate(n):
                return True
        return False

    def match(self, numbers):
        match = []
        for field, template in self.templates.items():
            if template.validate_all(numbers):
                match.append(field)
        return match