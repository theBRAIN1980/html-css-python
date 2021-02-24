var date = new Date()

var hour = date.getHours()

if (hour < 11) {
    document.write("Buna dimineata!")
} else if(hour < 18) {
    document.write("Buna ziua!")
} else {
    document.write("<h1>Buna seara!</h1>")
}