/**-----------------------------------------------------------------------
 * useGames.js
 * Matthew Kruse
 *
 * Game Hooks
 *-----------------------------------------------------------------------*/

import { API_URL } from "../constants";
import {useState, useEffect} from "react";

export function useGameList() {

    // Create states for Games, loading, and error
    const [games, setGames] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // Fetch games from the API
    useEffect(() => {
        setLoading(true);
        fetch(`${API_URL}/games/`, {
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then((response) => {
            if (response.ok) {
                return response.json();
            }
            setLoading(false);
            throw new Error('Network response was not ok');
        })
        .then(json => {
            setLoading(false);
            setGames(json);
        })
        .catch((error) => {
            setError(error);
        });
    }, []);

    return {
        games,
        loading,
        error};
}