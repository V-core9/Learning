function getValue(): string | undefined {
    return 'hello';
}
let value = getValue();
console.log('value length: ' + value!.length);