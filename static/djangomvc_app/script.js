document.addEventListener("DOMContentLoaded", async () => {
    const messageElement = document.getElementById('message');
    
    try {
        const response = await fetch('/api/message/');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        messageElement.textContent = data.message;
    } catch (error) {
        console.error("Error fetching message:", error);
        messageElement.textContent = "Failed to load message. Please try again.";
    }
});