function getGrade(score) {
    let grade;
    // Write your code here
    if (score > 25) {
        grade = 'A'
    }
    else if (score > 20) {
        grade = 'B'
    }
    else if (score > 15) {
        grade = 'C'
    }
    else if (score > 10) {
        grade = 'D'
    }
    else if (score > 5) {
        grade = 'E'
    }
    else if (score <= 5) {
        grade = 'F'
    }
    return grade;
}


function main() {
    const score = +(readLine());
    
    console.log(getGrade(score));
}