# Question 1: Animal, Dog, and Cat Classes

class Animal:
    def speak(self):
        return None

class Dog(Animal):
    def speak(self):
        return 'bark'

class Cat(Animal):
    def speak(self):
        return 'meow'

# Example usage
dog = Dog()
cat = Cat()

print(dog.speak())  # Output: 'bark'
print(cat.speak())  # Output: 'meow'
