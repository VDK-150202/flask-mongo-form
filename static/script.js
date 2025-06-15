document.getElementById("myForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const formData = {
        name: this.name.value,
        email: this.email.value
    };

    const response = await fetch("/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
    });

    const result = await response.json();
    if (response.ok) {
        window.location.href = "/success";
    } else {
        document.getElementById("error-message").innerText = result.error || "Something went wrong.";
    }
});
