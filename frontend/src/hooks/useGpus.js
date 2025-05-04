/**-----------------------------------------------------------------------
 * useGpus.js
 * Matthew Kruse
 *
 * GPU Hooks
 *-----------------------------------------------------------------------*/

import { API_URL } from "../constants";
import {useState, useEffect} from "react";

export function useGpuList() {

    // Create states for GPUs, loading, and error
    const [gpus, setGpus] = useState([]);
    const [filteredGpus, setFilteredGpus] = useState([]);
    const [selectedGpuManufacturerFilter, setSelectedGpuManufacturerFilter] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // Fetch gpus from the API
    useEffect(() => {
        setLoading(true);
        fetch(`${API_URL}/gpus/`, {
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
            setGpus(json);
            setFilteredGpus(json);
        })
        .catch((error) => {
            setError(error);
        });
    }, []);

    // Filter GPUs by manufacturer and series
    useEffect(() => {
        let filtered = gpus;

        // Filter by manufacturer if one is selected
        if (selectedGpuManufacturerFilter) {
            filtered = filtered.filter(gpu => gpu.manufacturer.trim() === selectedGpuManufacturerFilter.trim());
        }

        setFilteredGpus(filtered);
    }, [gpus, selectedGpuManufacturerFilter]);

        // Function to set the selected manufacturer and reset year
    const filterByGpuManufacturer = (manufacturer) => {
        setSelectedGpuManufacturerFilter(manufacturer);
    };

    // Function to set the selected series
    return {
        gpus,
        filteredGpus,
        selectedGpuManufacturerFilter: selectedGpuManufacturerFilter,
        filterByGpuManufacturer: filterByGpuManufacturer,
        loading,
        error};
}