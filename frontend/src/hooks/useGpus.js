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
    const [selectedGpuYearFilter, setSelectedGpuYearFilter] = useState("");
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

       // Filter by year if one is selected (and after applying manufacturer filter)
        if (selectedGpuYearFilter) {
            filtered = filtered.filter(gpu => gpu.year === Number(selectedGpuYearFilter));
        }

        setFilteredGpus(filtered);
    }, [gpus, selectedGpuManufacturerFilter, selectedGpuYearFilter]);

        // Function to set the selected manufacturer and reset year
    const filterByGpuManufacturer = (manufacturer) => {
        setSelectedGpuManufacturerFilter(manufacturer);
        setSelectedGpuYearFilter("");
    };

    // Function to set the selected series
    const filterByGpuYear = (year) => {
        setSelectedGpuYearFilter(year);
    };
    return {
        gpus,
        filteredGpus,
        selectedGpuManufacturerFilter: selectedGpuManufacturerFilter,
        selectedGpuYearFilter: selectedGpuYearFilter,
        filterByGpuManufacturer: filterByGpuManufacturer,
        filterByGpuYear: filterByGpuYear,
        loading,
        error};
}