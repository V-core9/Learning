# TS Intro [w3schools]

## Intro

TypeScript allows developers to add types to JavaScript

JavaScript is a loosely typed language

## Get Started

### The TypeScript compiler can be configured with which file?

- tsconfig.json

## Simple Types

### There are two main ways TypeScript assigns a type

1. Explicit
2. Implicit

### Implicit example

> Create a "firstName" variable, string type using Implicit type

    let firstName = "Dylan";

### Explicit example

> Create a "firstName" variable, string type using Explicit type

    let firstName:string = "Dylan";

## TypeScript Special Types

TypeScript has special types that may not refer to any specific type of data.

### Type: any

any is a type that disables type checking and effectively allows all types to be used.

    let v: any = true;
    v = "string"; // no error as it can be "any" type
    Math.round(v); // no error as it can be "any" type

> any can be a useful way to get past errors since it disables type checking, but TypeScript will not be able provide type safety, and tools which rely on type data, such as auto completion, will not work. Remember, it should be avoided at "any" cost...

### Type: unknown

unknown is a similar, but safer alternative to any.

    let w: unknown = 1;
    w = "string"; // no error
    w = {
      runANonExistentMethod: () => {
        console.log("I think therefore I am");
      }
    } as { runANonExistentMethod: () => void}
    // How can we avoid the error for the code commented out below when we don't know the type?
    // w.runANonExistentMethod(); // Error: Object is of type 'unknown'.
    if(typeof w === 'object' && w !== null) {
      (w as { runANonExistentMethod: Function }).runANonExistentMethod();
    }
    // Although we have to cast multiple times we can do a check in the if to secure our type and have a safer casting

>unknown is best used when you don't know the type of data being typed. To add a type later, you'll need to cast it.
>
>Casting is when we use the "as" keyword to say property or variable is of the casted type.

### Type: never

never effectively throws an error whenever it is defined.

    let x: never = true; // Error: Type 'boolean' is not assignable to type 'never'.

> never is rarely used, especially by itself, its primary use is in advanced generics.

### Type: undefined & null

undefined and null are types that refer to the JavaScript primitives undefined and null respectively.

    let y: undefined = undefined;
    let z: null = null;

> These types don't have much use unless strictNullChecks is enabled in the tsconfig.json file.

## TypeScript Arrays

TypeScript has a specific syntax for typing arrays.

    const names: string[] = [];
    names.push("Dylan"); // no error
    // names.push(3); // Error: Argument of type 'number' is not assignable to parameter of type 'string'.

> Run it: **npx ts-node TypeScript/Arrays/intro.ts**

### Readonly

The readonly keyword can prevent arrays from being changed.

    const names: readonly string[] = ["Dylan"];
    names.push("Jack"); // Error: Property 'push' does not exist on type 'readonly string[]'.
    // try removing the readonly modifier and see if it works?

> Run it: **npx ts-node TypeScript/Arrays/Readonly.ts**

### Type Inference

TypeScript can infer the type of an array if it has values.

    const numbers = [1, 2, 3]; // inferred to type number[]
    numbers.push(4); // no error
    // comment line below out to see the successful assignment
    numbers.push("2"); // Error: Argument of type 'string' is not assignable to parameter of type 'number'.
    let head: number = numbers[0]; // no error

> Run it: **npx ts-node TypeScript/Arrays/Inference.ts**

## TypeScript Tuples

### Typed Arrays

A tuple is a typed array with a pre-defined length and types for each index.

Tuples are great because they allow each element in the array to be a known type of value.

To define a tuple, specify the type of each element in the array:

    // define our tuple
    let ourTuple: [number, boolean, string];

    // initialize correctly
    ourTuple = [5, false, 'Coding God was here'];

As you can see we have a number, boolean and a string. But what happens if we try to set them in the wrong order:

    // define our tuple
    let ourTuple: [number, boolean, string];

    // initialized incorrectly which throws an error
    ourTuple = [false, 'Coding God was mistaken', 5];

> Run it: **npx ts-node TypeScript/Tuple/intro.ts**

> Even though we have a boolean, string, and number the order matters in our tuple and will throw an error.

### Readonly Tuple

A good practice is to make your tuple readonly.

Tuples only have strongly defined types for the initial values:

    // define our tuple
    let ourTuple: [number, boolean, string];
    // initialize correctly
    ourTuple = [5, false, 'Coding God was here'];
    // We have no type safety in our tuple for indexes 3+
    ourTuple.push('Something new and wrong');
    console.log(ourTuple);

You see the new valueTuples only have strongly defined types for the initial values

    // define our readonly tuple
    const ourReadonlyTuple: readonly [number, boolean, string] = [5, true, 'The Real Coding God'];
    // throws error as it is readonly.
    ourReadonlyTuple.push('Coding God took a day off');

> Run it: **npx ts-node TypeScript/Tuple/Readonly.ts**

>If you have ever used React before you have worked with tuples more than likely.
>
> **useState** returns a tuple of the value and a setter function.
>
> **const [firstName, setFirstName] = useState('Dylan')** is a common example.
>
>Because of the structure we know our first value in our list will be a certain value type in this case a string and the second value a function.

### Named Tuples

**Named tuples** allow us to provide context for our values at each index.

    const graph: [x: number, y: number] = [55.2, 41.3];

> **Named tuples** provide more context for what our index values represent.

> Run it: **npx ts-node TypeScript/Tuple/Named.ts**

### Destructuring Tuples

Since tuples are arrays we can also destructure them.

    const graph: [number, number] = [55.2, 41.3];
    const [x, y] = graph;

> Run it: **npx ts-node TypeScript/Tuple/Destructuring.ts**

## TypeScript Object Types

TypeScript has a specific syntax for typing objects.

    const car: { type: string, model: string, year: number } = {
        type: "Toyota",
        model: "Corolla",
        year: 2009
    };

> Run it: **npx ts-node TypeScript/Object/intro.ts**

> Object types like this can also be written separately, and even be reused, look at interfaces for more details.

### Type Inference

TypeScript can infer the types of properties based on their values.

    const car = {
        type: "Toyota",
    };
    car.type = "Ford"; // no error
    car.type = 2; // Error: Type 'number' is not assignable to type 'string'.

> Run it: **npx ts-node TypeScript/Object/intro_Inference.ts**

### Optional Properties

Optional properties are properties that don't have to be defined in the object definition.

#### Example without an optional property

    const car: { type: string, mileage: number } = { // Error: Property 'mileage' is missing in type '{ type: string; }' but required in type '{ type: string; mileage: number; }'.
        type: "Toyota",
    };
    car.mileage = 2000;

> Run it: **npx ts-node TypeScript/Object/without_optional.ts**

#### Example with an optional property

    const car: { type: string, mileage?: number } = { // no error
        type: "Toyota"
    };
    car.mileage = 2000;

> Run it: **npx ts-node TypeScript/Object/with_optional.ts**
