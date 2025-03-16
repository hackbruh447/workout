document.addEventListener('DOMContentLoaded', function () {
    // Fetch data from the Django view
    fetch('get_user_data')
        .then(response => response.json())  // Parse JSON response
        .then(data => {
            const points = data.points;
            const usernames = data.usernames;

            console.log(points);  // Debugging: check if points array is passed correctly
            console.log(usernames);  // Debugging: check if usernames array is passed correctly

            // Function to create a new div for each user
            function createUserDiv(username, point) {
                const userDiv = document.createElement('div');
                userDiv.classList.add('user');  // You can add a CSS class to style the div

                // Add user details to the div
                userDiv.innerHTML = `
                    <h3>${username}</h3>
                    <p>Points: ${point}</p>
                `;
                
                return userDiv;
            }

            // Get the user container in the DOM
            const userContainer = document.getElementById('user-container');

            // Iterate over the points and usernames lists to create divs for each user
            for (let i = 0; i < points.length; i++) {
                const username = usernames[i];
                const point = points[i];
                const userDiv = createUserDiv(username, point);
                userContainer.appendChild(userDiv);
            }
        })
    

    }
)