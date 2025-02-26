const ladder = document.getElementById('ladder');

// Function to fetch and display the ladder with tiers
function fetchAndDisplayLadder(file) {
    fetch(file)
        .then(response => response.text())
        .then(data => {
            ladder.innerHTML = ''; // Clear the current ladder
            const players = data.split('\n').filter(player => player.trim() !== '');
            
            // Initialize tier thresholds
            const tiers = {
                "Tier 1": 5,
                "Tier 2": 20,
                "Tier 3": players.length
            };

            let currentTier = null;
            players.forEach((player, index) => {
                // Determine the player's tier
                let tier = null;
                if (index + 1 <= tiers["Tier 1"]) {
                    tier = "Tier 1";
                } else if (index + 1 <= tiers["Tier 2"]) {
                    tier = "Tier 2";
                } else {
                    tier = "Tier 3";
                }

                // Add a tier heading if it changes
                if (tier !== currentTier) {
                    currentTier = tier;

                    // Create a tier heading
                    const tierHeading = document.createElement('div');
                    tierHeading.classList.add('tier-heading');
                    tierHeading.innerText = currentTier;
                    ladder.appendChild(tierHeading);
                }

                // Split player data by whitespace (assuming format: "FirstName LastName Wins Losses")
                const parts = player.trim().split(' ');
                const name = parts.slice(0, -2).join(' '); // Combine all parts except the last two as the name
                
                const tokens_avail = parts[parts.length - 1]; // Last part is losses

                // Create a list item with the parsed data
                const playerItem = document.createElement('li');
                playerItem.innerHTML = `
                    <span class="rank">${index + 1}</span>
                    <span class="name">${name}</span>
                    <span class="wl">${tokens_avail}</span>
                `;
                ladder.appendChild(playerItem);
            });
        })
        .catch(error => console.error('Error fetching player list:', error));
}

// Event listeners for toggle buttons
document.getElementById('guys-ladder-btn').addEventListener('click', () => {
    document.getElementById('guys-ladder-btn').classList.add('active');
    document.getElementById('girls-ladder-btn').classList.remove('active');
    fetchAndDisplayLadder('s25_guys_ladder.txt');
});

document.getElementById('girls-ladder-btn').addEventListener('click', () => {
    document.getElementById('girls-ladder-btn').classList.add('active');
    document.getElementById('guys-ladder-btn').classList.remove('active');
    fetchAndDisplayLadder('s25_girls_ladder.txt');
});

// Default to guys ladder on page load
fetchAndDisplayLadder('s25_guys_ladder.txt');

