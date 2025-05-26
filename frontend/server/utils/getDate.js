export default function getDate(dateString) {
    try {
        console.debug("Parsing date:", dateString);
        const date = new Date(dateString);
        let day = date.getDate();
        let year = date.getFullYear();
        let month = date.getMonth() + 1;
        return `${year}-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
    }
    catch (error) {
        console.error("Error parsing date:", error);
        return null;
    }
}