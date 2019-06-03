function getLetter(s) {
    let letter;
    let first = s[0];
    // Write your code here
    switch (true) {
        case 'aeiou'.includes(first):
            // code block
            letter = 'A'
            break;
        case 'bcdefg'.includes(first):
            // code block
            letter = 'B'
            break;
        case 'hijklm'.includes(first):
            // code block
            letter = 'C'
            break;
        case 'nopqrstuvwxyz'.includes(first):
            // code block
            letter = 'D'
            break;
    }
    
    return letter;
}