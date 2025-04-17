/**-----------------------------------------------------------------------
 * useCpus.js
 * Matthew Kruse
 *
 * CPU Hooks
 *-----------------------------------------------------------------------*/

import { API_URL } from "../constants";
import {useState, useEffect} from "react";

export function useCpuList() {

    // Create states for CPUs, loading, and error
    const [cpus, setCpus] = useState([]);
    const [filteredCpus, setFilteredCpus] = useState([]);
    const [selectedManufacturerFilter, setSelectedManufacturerFilter] = useState("");
    const [selectedCpuSeriesFilter, setSelectedCpuSeriesFilter] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // Fetch cpus from the API
    useEffect(() => {
        setLoading(true);
        fetch(`${API_URL}/cpus/`, {
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
            setCpus(json);
            setFilteredCpus(json);
        })
        .catch((error) => {
            setError(error);
        });
    }, []);

    // Filter CPUs by manufacturer and series
    useEffect(() => {
        let filtered = cpus;

        // Filter by manufacturer if one is selected
        if (selectedManufacturerFilter) {
            filtered = filtered.filter(cpu => cpu.manufacturer.trim() === selectedManufacturerFilter.trim());
        }

        // Filter by series if one is selected (and after applying manufacturer filter)
        if (selectedCpuSeriesFilter) {
            filtered = filtered.filter(cpu => cpu.series === selectedCpuSeriesFilter);
        }

        setFilteredCpus(filtered);
    }, [cpus, selectedManufacturerFilter, selectedCpuSeriesFilter]);

        // Function to set the selected manufacturer and reset series
    const filterByManufacturer = (manufacturer) => {
        setSelectedManufacturerFilter(manufacturer);
        setSelectedCpuSeriesFilter("");
    };

    // Function to set the selected series
    const filterByCpuSeries = (series) => {
        setSelectedCpuSeriesFilter(series);
    };


    return {
        cpus,
        filteredCpus,
        selectedCpuManufacturerFilter: selectedManufacturerFilter,
        selectedCpuSeriesFilter: selectedCpuSeriesFilter,
        filterByCpuManufacturer: filterByManufacturer,
        filterByCpuSeries: filterByCpuSeries,
        cpuLoading: loading,
        cpuError: error};
}