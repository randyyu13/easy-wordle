const localURL = 'http://localhost:8000'; // Adjust this to your actual API base URL
const wordDataApiUrl = 'https://api.datamuse.com'

// Helper function to handle API requests
async function apiRequest(apiBaseUrl,endpoint, method = 'GET', body = null) {
    const headers = { 'Content-Type': 'application/json' };
    const options = { method, headers };

    if (body) {
        options.body = JSON.stringify(body);
    }

    const response = await fetch(`${apiBaseUrl}${endpoint}`, options);
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
}

// User-related API calls
export async function createUser(url, userData) {
    return apiRequest(url, '/new-user', 'POST', userData);
}

// Game-related API calls
export async function createGame(url, gameData) {
    return apiRequest(url, '/new-game', 'POST', gameData);
}

// Word-related API calls
export async function setWordOfTheDay(url) {
    return apiRequest(url, '/set-word-of-the-day', 'POST');
}

export async function getWordOfTheDay(url) {
    return apiRequest(url, `/word-of-the-day/`);
}

export async function getGameByUserId(url, userId) {
    return apiRequest(url, `/game-data?user_id=${userId}`);
}

export async function upsertGame(url, gameData) {
    return apiRequest(url, `/game-data/`, 'PATCH', gameData);
}

export async function isRealWord(url, word) {
    return apiRequest(url, `/words?sp=${word}&max=1`);
}

export { localURL, wordDataApiUrl, createUser, createGame, setWordOfTheDay, getWordOfTheDay, getGameByUserId, upsertGame, isRealWord }