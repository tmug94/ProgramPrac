// MM/DD/YYYY format
function getDayName(dateString) {
    var weekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    var date1 = new Date(dateString)
    return weekDays[date1.getUTCDay()];
}
