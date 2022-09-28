interface Person {
    name: string;
    age: number;
    location?: string;
}

const bob: Omit<Person, 'age' | 'location'> = {
    name: 'Bob'
    // `Omit` has removed age and location from the type and they can't be defined here
};