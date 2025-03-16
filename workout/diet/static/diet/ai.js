document.addEventListener("DOMContentLoaded", function () {
    let totalPoints = 0;
    const pointsDisplay = document.getElementById("points");
  
    // Attach event listeners to all "Complete" buttons
    const completeButtons = document.querySelectorAll(".complete-btn");
  
    completeButtons.forEach((btn) => {
      btn.addEventListener("click", function () {
        // Locate the challenge container
        const challengeDiv = btn.closest(".challenge");
        // Extract the points value from the text ("Points: X")
        const pointsText = challengeDiv.querySelector(".challenge-points").textContent;
        const pointsValue = parseInt(pointsText.replace("Points: ", ""), 10);
        
        totalPoints += pointsValue;
        pointsDisplay.textContent = totalPoints;
  
        // Mark the challenge as completed
        btn.disabled = true;
        btn.textContent = "Completed";
        btn.style.backgroundColor = "gray";
      });
    });
  });
  