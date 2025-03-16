document.addEventListener("DOMContentLoaded", function () {
    // Constants
    const caloricGoal = 2000;
    const POINTS_PER_CHALLENGE = 10;
    let consumedCalories = 0;
    let challengesCompleted = 0;
    let totalPoints = 0;
    let userScore = 0;

    // DOM Elements
    const caloricIntakeInput = document.getElementById("caloric-intake-input");
    const submitCaloriesButton = document.getElementById("submit-calories");
    const leftoverCaloriesValue = document.getElementById("leftover-calories-value");
    const totalCaloriesValue = document.getElementById("total-calories");
    const challengesCompletedValue = document.getElementById("challenges-completed");
    const totalPointsValue = document.getElementById("total-points");
    const userScoreValue = document.getElementById("user-score");
    const leaderboardList = document.getElementById("leaderboard-list");

    // Fetch leaderboard data from the database
    function fetchLeaderboard() {
        fetch('get_user_data')
            .then(response => response.json())
            .then(data => {
                const points = data.points;
                const usernames = data.usernames;

                // Clear existing leaderboard
                leaderboardList.innerHTML = "";

                // Create and append leaderboard items
                points.forEach((point, index) => {
                    const li = document.createElement("li");
                    li.classList.add("leaderboard-item");

                    li.innerHTML = `
                        <span class="rank">${index + 1}</span>
                        <span class="name">${usernames[index]}</span>
                        <span class="score">${point}</span>
                    `;

                    // Highlight current user
                    if (usernames[index] === "YOU") {
                        li.classList.add("current-user");
                    }

                    leaderboardList.appendChild(li);
                });
            })
            .catch(error => console.error("Error fetching leaderboard data:", error));
    }

    // Function to update the leftover calories
    function updateLeftoverCalories() {
        leftoverCaloriesValue.textContent = caloricGoal - consumedCalories;
    }

    // Function to update total caloric intake display
    function updateTotalCaloricIntake() {
        totalCaloriesValue.textContent = consumedCalories;
    }

    // Function to handle caloric intake submission
    function handleCaloricIntake() {
        const inputValue = caloricIntakeInput.value.trim();

        if (!inputValue || isNaN(inputValue)) {
            alert("Please enter a valid number of calories.");
            return;
        }

        const calories = parseInt(inputValue, 10);
        if (calories < 0) {
            alert("Calories cannot be negative.");
            return;
        }

        consumedCalories += calories;
        updateLeftoverCalories();
        updateTotalCaloricIntake();
        caloricIntakeInput.value = "";
    }

    // Function to handle challenge toggling
    function handleChallengeCompletion(event) {
        const checkmark = event.target.closest(".challenge-check");
        const wasCompleted = checkmark.classList.contains("completed");

        // Toggle completed state
        checkmark.classList.toggle("completed");

        // Update counters based on new state
        if (checkmark.classList.contains("completed")) {
            challengesCompleted++;
            totalPoints += POINTS_PER_CHALLENGE;
            userScore += POINTS_PER_CHALLENGE;
        } else {
            challengesCompleted = Math.max(0, challengesCompleted - 1);
            totalPoints = Math.max(0, totalPoints - POINTS_PER_CHALLENGE);
            userScore = Math.max(0, userScore - POINTS_PER_CHALLENGE);
        }

        // Update displays
        challengesCompletedValue.textContent = challengesCompleted;
        totalPointsValue.textContent = totalPoints;
        userScoreValue.textContent = userScore;

        // Update leaderboard
        fetchLeaderboard();
    }

    // Event listeners
    document.querySelectorAll(".challenge-check").forEach(checkmark => {
        checkmark.addEventListener("click", handleChallengeCompletion);
    });

    submitCaloriesButton.addEventListener("click", handleCaloricIntake);
    caloricIntakeInput.addEventListener("keypress", (event) => {
        if (event.key === "Enter") handleCaloricIntake();
    });

    // Initialize displays
    updateLeftoverCalories();
    updateTotalCaloricIntake();
    fetchLeaderboard(); // Fetch and display leaderboard data
});