document.addEventListener("DOMContentLoaded", function () {
    let totalPoints = 0;
    const pointsDisplay = document.getElementById("points");
  
    // Attach event listeners to all "Complete" buttons
    const completeButtons = document.querySelectorAll(".complete-btn");
  
    completeButtons.forEach((btn) => {
      btn.addEventListener("click", function () {
        // Locate the challenge container
        const challengeDiv = btn.closest(".challenge")
        totalPoints = document.querySelector("#points").innerHTML
        let user = document.querySelector("#kwab").innerHTML;
        // Extract the points value from the text ("Points: X")
        const pointsText = challengeDiv.querySelector(".challenge-points").textContent;
        const pointsValue = parseInt(pointsText.replace("Points: ", ""), 10);
        console.log(user)
        
        fetch("update_points",{
          method: "POST",

          body: JSON.stringify({
          user: user,
          points: pointsValue,
          })
        })
        .then(response => response.json())
        .then(data => {
          console.log(data);
        })
        
        totalPoints = Number(totalPoints) + Number(pointsValue);

        pointsDisplay.textContent = totalPoints;
  
        // Mark the challenge as completed
        btn.disabled = true;
        btn.textContent = "Completed";
        btn.style.backgroundColor = "gray";
      });
    });
  });
  