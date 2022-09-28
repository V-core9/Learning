class Person {
    // name is a private member variable
    public constructor(private name: string) { }

    public getName(): string {
        return this.name;
    }
}

const person = new Person("Jane");
console.log(person.getName());