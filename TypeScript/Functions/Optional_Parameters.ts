// the `?` operator here marks parameter `c` as optional
function add(a: number, b: number, c?: number): number {
    return a + b + (c || 0);
}

console.log(add(10, 20));

console.log(add(10, 20, 30));