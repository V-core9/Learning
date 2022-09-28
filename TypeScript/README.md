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

### Index Signatures

Index signatures can be used for objects without a defined list of properties.

    const nameAgeMap: { [index: string]: number } = {};
    nameAgeMap.Jack = 25; // no error
    nameAgeMap.Mark = "Fifty"; // Error: Type 'string' is not assignable to type 'number'.

> Run it: **npx ts-node TypeScript/Object/Index_Signatures.ts**

>Index signatures like this one can also be expressed with utility types like Record<string, number>.  
>Learn more about utility types like this in our TypeScript Utility Types chapter.

## TypeScript Enums

An enum is a special "class" that represents a group of constants (unchangeable variables).

Enums come in two flavors string and numeric. Lets start with numeric.

### Numeric Enums - Default

By default, enums will initialize the first value to 0 and add 1 to each additional value

    enum CardinalDirections {
        North,
        East,
        South,
        West
    }
    let currentDirection = CardinalDirections.North;
    // logs 0
    console.log(currentDirection);
    // throws error as 'North' is not a valid enum
    currentDirection = 'North'; // Error: "North" is not assignable to type 'CardinalDirections'.

> Run it: **npx ts-node TypeScript/Enums/Default.ts**

### Numeric Enums - Initialized

You can set the value of the first numeric enum and have it auto increment from that

    enum CardinalDirections {
        North = 1,
        East,
        South,
        West
    }
    // logs 1
    console.log(CardinalDirections.North);
    // logs 4
    console.log(CardinalDirections.West);

> Run it: **npx ts-node TypeScript/Enums/Initialized.ts**

### Numeric Enums - Fully Initialized

You can assign unique number values for each enum value. Then the values will not incremented automatically

    enum StatusCodes {
        NotFound = 404,
        Success = 200,
        Accepted = 202,
        BadRequest = 400
    }
    // logs 404
    console.log(StatusCodes.NotFound);
    // logs 200
    console.log(StatusCodes.Success);

> Run it: **npx ts-node TypeScript/Enums/Fully_Initialized.ts**

### String Enums

Enums can also contain strings. This is more common than numeric enums, because of their readability and intent.

    enum CardinalDirections {
        North = 'North',
        East = "East",
        South = "South",
        West = "West"
    };
    // logs "North"
    console.log(CardinalDirections.North);
    // logs "West"
    console.log(CardinalDirections.West);

> Run it: **npx ts-node TypeScript/Enums/String.ts**

> Technically, you can mix and match string and numeric enum values, but it is recommended not to do so.

## TypeScript Type Aliases and Interfaces

TypeScript allows types to be defined separately from the variables that use them.

Aliases and Interfaces allows types to be easily shared between different variables/objects.

### Type Aliases

Type Aliases allow defining types with a custom name (an Alias).

Type Aliases can be used for primitives like **string** or more complex types such as **objects** and **arrays**

    type CarYear = number
    type CarType = string
    type CarModel = string
    type Car = {
        year: CarYear,
        type: CarType,
        model: CarModel
    }

    const carYear: CarYear = 2001
    const carType: CarType = "Toyota"
    const carModel: CarModel = "Corolla"
    const car: Car = {
        year: carYear,
        type: carType,
        model: carModel
    };

> Run it: **npx ts-node TypeScript/Aliases_Interfaces/Aliases.ts**

### Interfaces

Interfaces are similar to type aliases, except they **only** apply to **object** types.

    interface Rectangle {
        height: number,
        width: number
    }

    const rectangle: Rectangle = {
        height: 20,
        width: 10
    };

> Run it: **npx ts-node TypeScript/Aliases_Interfaces/Interfaces.ts**

### Extending Interfaces

Interfaces can extend each other's definition.

> Extending an interface means you are creating a new interface with the same properties as the original, plus something new.

    interface Rectangle {
        height: number,
        width: number
    }

    interface ColoredRectangle extends Rectangle {
        color: string
    }

    const coloredRectangle: ColoredRectangle = {
        height: 20,
        width: 10,
        color: "red"
    };

> Run it: **npx ts-node TypeScript/Aliases_Interfaces/Extending.ts**

## TypeScript Union Types

**Union types** are used when a value can be more than a single type.

Such as when a property would be **string** or **number**.

### Union | (OR)

Using the **|** we are saying our parameter is a **string** or **number**

    function printStatusCode(code: string | number) {
        console.log(`My status code is ${code}.`)
    }
    printStatusCode(404);
    printStatusCode('404');

> Run it: **npx ts-node TypeScript/Union/intro.ts**

### Union Type Errors

> Note: you need to know what your type is when union types are being used to avoid type errors:

    function printStatusCode(code: string | number) {
        console.log(`My status code is ${code.toUpperCase()}.`) // error: Property 'toUpperCase' does not exist on type 'string | number'. Property 'toUpperCase' does not exist on type 'number'
    }

> Run it: **npx ts-node TypeScript/Union/errors.ts**

## TypeScript Functions

TypeScript has a specific syntax for typing function parameters and return values.

### Return Type

The type of the value returned by the function can be explicitly defined.

    // the `: number` here specifies that this function returns a number
    function getTime(): number {
        return new Date().getTime();
    }

> If no return type is defined, TypeScript will attempt to infer it through the types of the variables or expressions returned.

> Run it: **npx ts-node TypeScript/Functions/Return.ts**

### Void Return Type

The type void can be used to indicate a function doesn't return any value.

    function printHello(): void {
        console.log('Hello!');
    }

> Run it: **npx ts-node TypeScript/Functions/void.ts**

### Parameters

Function parameters are typed with a similar syntax as variable declarations.

    function multiply(a: number, b: number) {
        return a * b;
    }

> If no parameter type is defined, TypeScript will default to using any, unless additional type information is available as shown in the Default Parameters and Type Alias sections below.

> Run it: **npx ts-node TypeScript/Functions/Parameters.ts**

### Optional Parameters

By default TypeScript will assume all parameters are required, but they can be explicitly marked as optional.

    // the `?` operator here marks parameter `c` as optional
    function add(a: number, b: number, c?: number) {
        return a + b + (c || 0);
    }

> Run it: **npx ts-node TypeScript/Functions/Optional_Parameters.ts**

### Default Parameters

For parameters with default values, the default value goes after the type annotation

    function pow(value: number, exponent: number = 10) {
        return value ** exponent;
    }

    console.log(pow(2));

TypeScript can also infer the type from the default value.

> Run it: **npx ts-node TypeScript/Functions/Default_Parameters.ts**

### Named Parameters

Typing named parameters follows the same pattern as typing normal parameters.

    function divide({ dividend, divisor }: { dividend: number, divisor: number }) {
        return dividend / divisor;
    }

    console.log(divide({ dividend: 100, divisor: 10 }));

> Run it: **npx ts-node TypeScript/Functions/Named_Parameters.ts**

### Rest Parameters

Rest parameters can be typed like normal parameters, but the type must be an array as rest parameters are always arrays.

    function add(a: number, b: number, ...rest: number[]) {
        return a + b + rest.reduce((p, c) => p + c, 0);
    }

    console.log(add(10, 20, 30, 40));

> Run it: **npx ts-node TypeScript/Functions/Rest_Parameters.ts**

### Type Alias

Function types can be specified separately from functions with type aliases.

These types are written similarly to arrow functions.

    type Negate = (value: number) => number;

    // in this function, the parameter `value` automatically gets assigned the type `number` from the type `Negate`
    const negateFunction: Negate = (value) => value * -1;
    
    console.log(negateFunction(10));

> Run it: **npx ts-node TypeScript/Functions/Type_Alias.ts**