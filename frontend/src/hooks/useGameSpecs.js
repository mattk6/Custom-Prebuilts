/**-----------------------------------------------------------------------
 * useGameSpecs.js
 * Matthew Kruse
 *
 * Game Spec Hook (Filtered by Game ID and Spec Type)
 *-----------------------------------------------------------------------*/

import { API_URL } from "../constants";
import { useState, useEffect } from "react";

export function useGameSpecs(gameId, specType) {
    // Create states for gameSpecs, loading, and error
    const [gameSpecs, setGameSpecs] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // Fetch filtered game specs from the API
    useEffect(() => {
        // Only fetch data if gameId and specType are provided
        if (!gameId || !specType) return;

        setLoading(true);
        fetch(`${API_URL}/game-specs?game=${gameId}&spec=${specType}`, {
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
            setGameSpecs(json);
        })
        .catch((error) => {
            setLoading(false);
            setError(error);
        });
    }, [gameId, specType]);

    return {
        gameSpecs,
        loading,
        error
    };
}