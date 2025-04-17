import './App.css'
import {useCpuList} from "./hooks/useCpus.js";
import {useGpuList} from "./hooks/useGpus.js";
import {useGameList} from "./hooks/useGames.js";
import {useState, useEffect} from "react";
import {useGameSpecs} from "./hooks/useGameSpecs.js";

function App() {

    // CPU List hook
    const {
        cpus,
        filteredCpus,
        selectedCpuManufacturerFilter,
        filterByCpuManufacturer,
        filterByCpuSeries,
        cpuLoading,
        cpuError
    } = useCpuList();

    // GPU List hook
    const {
        gpus,
        filteredGpus,
        selectedGpuManufacturerFilter,
        filterByGpuManufacturer,
        filterByGpuYear,
        gpuLoading,
        gpuError
    } = useGpuList();

    // Game List hook
    const {
        games,
        gameLoading,
        gameError
    } = useGameList();

    // Game Specs hook

    // Equipment filters
    const gpuManufacturers = [...new Set(gpus.map(gpu => gpu.manufacturer))]

    const cpuManufacturers = [...new Set(cpus.map(cpu => cpu.manufacturer))]

    const cpuSeriesOptions = selectedCpuManufacturerFilter
        ? [...new Set(cpus
            .filter(cpu => cpu.manufacturer.trim() === selectedCpuManufacturerFilter.trim())
            .map(cpu => cpu.series))]
        : [];

    const gpuYearOptions = selectedGpuManufacturerFilter
        ? [...new Set(gpus
            .filter(gpu => gpu.manufacturer.trim() === selectedGpuManufacturerFilter.trim())
            .map(gpu => gpu.year))]
        : [];

    // Selection controls

    // state for drop down selections
    const [selectedCpuManufacturer, setSelectedCpuManufacturer] = useState("")
    const [selectedCpuSeries, setSelectedCpuSeries] = useState("")
    const [selectedCpuModel, setSelectedCpuModel] = useState("")
    const [selectedGpuManufacturer, setSelectedGpuManufacturer] = useState("")
    const [selectedGpuYear, setSelectedGpuYear] = useState("")
    const [selectedGpuModel, setSelectedGpuModel] = useState("")

    // Constants for the specification
    const SPEC_MINIMUM = 1;
    const SPEC_RECOMMENDED = 2;

    // State for selected specification (Minimum/Recommended)

    const [selectedSpec, setSelectedSpec] = useState(SPEC_MINIMUM);
    const [selectedDisplayResolution, setSelectedDisplayResolution] = useState("");

    const [selectedGame, setSelectedGame] = useState({id: 85});

    const { gameSpecs, gameSpecLoading, gameSpecError } = useGameSpecs(selectedGame.id, selectedSpec);

    // fetch from local storage
    useEffect(() => {
        const storedCpuManufacturer = localStorage.getItem("selectedCpuManufacturer");
        if (storedCpuManufacturer) {
            setSelectedCpuManufacturer(storedCpuManufacturer);
            filterByCpuManufacturer(storedCpuManufacturer);
        }

        const storedCpuSeries = localStorage.getItem("selectedCpuSeries");
        if (storedCpuSeries) {
            setSelectedCpuSeries(storedCpuSeries);
            filterByCpuSeries(storedCpuSeries);
        }

        const storedCpuModel = localStorage.getItem("selectedCpuModel");
        if (storedCpuModel) {
            setSelectedCpuModel(storedCpuModel);
        }

        const storedGpuManufacturer = localStorage.getItem("selectedGpuManufacturer");
        if (storedGpuManufacturer) {
            setSelectedGpuManufacturer(storedGpuManufacturer);
            filterByGpuManufacturer(storedGpuManufacturer);
        }

        const storedGpuYear = localStorage.getItem("selectedGpuYear");
        if (storedGpuYear) {
            setSelectedGpuYear(storedGpuYear);
            filterByGpuYear(storedGpuYear);
        }
        const storedGpuModel = localStorage.getItem("selectedGpuModel");
        if (storedGpuModel) {
            setSelectedGpuModel(storedGpuModel);
        }

        const storedDisplayResolution = localStorage.getItem("selectedDisplayResolution");
        if (storedDisplayResolution) {
            setSelectedDisplayResolution(storedDisplayResolution);
        }

    }, []);


    // save values to local storage as values change
    useEffect(() => {
        if(selectedCpuManufacturer) {
            localStorage.setItem("selectedCpuManufacturer", selectedCpuManufacturer);
        }
    }, [selectedCpuManufacturer]);

    useEffect(() => {
        if(selectedCpuSeries) {
            localStorage.setItem("selectedCpuSeries", selectedCpuSeries);
        }
    }, [selectedCpuSeries]);

    useEffect(() => {
        if(selectedCpuModel) {
            localStorage.setItem("selectedCpuModel", selectedCpuModel);
        }
    }, [selectedCpuModel]);

    useEffect(() => {
       if(selectedGpuManufacturer && selectedGpuManufacturer!=="") {
           console.log("Saving GPU Manufacturer:", selectedGpuManufacturer);
           localStorage.setItem("selectedGpuManufacturer", selectedGpuManufacturer);
       }
    }, [selectedGpuManufacturer]);

    useEffect(() => {
        if(selectedGpuYear) {
            localStorage.setItem("selectedGpuYear", selectedGpuYear);
        }
    }, [selectedGpuYear]);


    useEffect(() => {
       if(selectedGpuModel) {
           localStorage.setItem("selectedGpuModel", selectedGpuModel);
       }
    }, [selectedGpuModel]);

    useEffect(() => {
       if(selectedDisplayResolution) {
           localStorage.setItem("selectedDisplayResolution", selectedDisplayResolution);
       }
    }, [selectedDisplayResolution]);

    useEffect(() => {
        if (selectedSpec) {
            localStorage.setItem("selectedSpec", selectedSpec);
        }
    }, [selectedSpec]);


    // Use a  loading, error, success pattern
    // This is a common pattern in React for handling async data fetching

    if (cpuLoading || gpuLoading || gameLoading || gameSpecLoading) {
        return (
            <>
                <h1>Loading...</h1>
            </>
        )
    }

    if (cpuError || gpuError || gameError || gameSpecError) {
        return (
            <>
                <h1>cpu Error(s): {cpuError.message}</h1>
                <h1>gpu Error(s): {gpuError.message}</h1>
                <h1>game Error(s): {gameError.message}</h1>
                <h1>game Error(s): {gameSpecError.message}</h1>
            </>
        )
    }

    // keys are used to tell react which item to update if data changes
    // so we don't have to re-render the entire list
    return (
        <>
            <div className="layout">
                <div className="container">
                    <h2 className="">Your Setup</h2>
                    <table className="form-table">
                        <thead>
                        <tr>
                            <th>CPU Manufacturer</th>
                            <th>CPU Series</th>
                            <th>CPU Model</th>
                            <th>GPU Manufacturer</th>
                            <th>GPU Year</th>
                            <th>GPU Model</th>
                            <th>Display Resolution</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>
                                <select
                                    id="cpu-manufacturer-select"
                                    value={selectedCpuManufacturer}
                                    onChange={(e) => {
                                        setSelectedCpuManufacturer(e.target.value)
                                        filterByCpuManufacturer(e.target.value)
                                    }}
                                >
                                    <option value="">All Manufacturers</option>
                                    {cpuManufacturers.map(manufacturer => (
                                        <option key={manufacturer} value={manufacturer}>
                                            {manufacturer}
                                        </option>
                                    ))}
                                </select>
                            </td>
                            <td>
                                <select
                                    id="cpu-series-select"
                                    value={selectedCpuSeries}
                                    onChange={(e) => {
                                        setSelectedCpuSeries(e.target.value)
                                        filterByCpuSeries(e.target.value)
                                    }}
                                    disabled={!selectedCpuManufacturer}
                                >
                                    <option value="">All Series</option>
                                    {cpuSeriesOptions.map(series => (
                                        <option key={series} value={series}>
                                            {series}
                                        </option>
                                    ))}
                                </select>
                            </td>

                            <td>
                                <select id="cpu-select"
                                        value={selectedCpuModel}
                                        onChange={(e) => {
                                            setSelectedCpuModel(e.target.value)
                                        }}
                                >
                                    {filteredCpus.map((cpu) => (
                                        <option key={cpu.id} value={cpu.id}>
                                            {cpu.name}
                                        </option>
                                    ))}
                                </select>
                            </td>

                            <td>
                                <select
                                    id="gpu-manufacturer-select"
                                    value={selectedGpuManufacturer}
                                    onChange={(e) => {
                                        setSelectedGpuManufacturer(e.target.value)
                                        filterByGpuManufacturer(e.target.value)
                                    }}
                                >
                                    <option value="">All Manufacturers</option>
                                    {gpuManufacturers.map(manufacturer => (
                                        <option key={manufacturer} value={manufacturer}>
                                            {manufacturer}
                                        </option>
                                    ))}
                                </select>
                            </td>

                            <td>
                                <select
                                    id="gpu-year-select"
                                    value={selectedGpuYear}
                                    onChange={(e) => {
                                        setSelectedGpuYear(e.target.value)
                                        filterByGpuYear(e.target.value)
                                    }}
                                    disabled={!selectedGpuManufacturer}
                                >
                                    <option value="">All Years</option>
                                    {gpuYearOptions.map(year => (
                                        <option key={year} value={year}>
                                            {year}
                                        </option>
                                    ))}
                                </select>
                            </td>


                            <td>
                                <select
                                    id="gpu-select"
                                    value={selectedGpuModel}
                                    onChange={(e) => {
                                        setSelectedGpuModel(e.target.value)
                                    }}
                                >
                                    {filteredGpus.map((gpu) => (
                                        <option key={gpu.id} value={gpu.id}>
                                            {gpu.name}
                                        </option>
                                    ))}
                                </select>
                            </td>
                            <td>
                                <select
                                    id="resolution-select"
                                    value={selectedDisplayResolution}
                                    onChange={(e) => {
                                        setSelectedDisplayResolution(e.target.value)
                                    }}
                                >
                                    <option value="">Select a Resolution</option>
                                    <optgroup label="High-End">
                                        <option value="3840x2160">3840x2160 (4K UHD)</option>
                                        <option value="3440x1440">3440x1440 (UltraWide QHD)</option>
                                        <option value="2560x1440">2560x1440 (QHD)</option>
                                    </optgroup>
                                    <optgroup label="Mid-Range">
                                        <option value="1920x1080">1920x1080 (Full HD)</option>
                                        <option value="2560x1080">2560x1080 (UltraWide FHD)</option>
                                        <option value="1600x900">1600x900 (HD+)</option>
                                    </optgroup>
                                    <optgroup label="Low-End">
                                        <option value="1366x768">1366x768 (HD)</option>
                                        <option value="1280x720">1280x720 (HD)</option>
                                        <option value="1024x768">1024x768 (XGA)</option>
                                    </optgroup>
                                </select>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
                <div className={"container"}>
                    <h2 className="">Game Check</h2>
                    <table className="form-table">
                        <thead>
                        <tr>
                            <th>Desired Game</th>
                            <th>Game Hardware Specification</th>
                            <th>System Compatibility</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>
                                <select
                                    id="game-select"
                                    value={selectedGame.id}
                                    onChange={(e) => {
                                        setSelectedGame({id: e.target.value});
                                    }}
                                >
                                    <option value="">All Games</option>
                                    {games.map((game) => (
                                        <option key={game.id} value={game.id}>
                                            {game.name}
                                        </option>
                                    ))}
                                </select>
                            </td>
                            <td>
                                <div className="radio-group">
                                    <label>
                                        <input
                                            type="radio"
                                            name="spec"
                                            value="1"
                                            onChange={() => setSelectedSpec(SPEC_MINIMUM)}
                                        />
                                        Minimum
                                    </label>
                                    <label>
                                        <input
                                            type="radio"
                                            name="spec"
                                            value="2"
                                            onChange={() => setSelectedSpec(SPEC_RECOMMENDED)}
                                        />
                                        Recommended
                                    </label>
                                </div>
                            </td>
                            <td>
                                <span className="compatibilityCheck">Yes</span>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
                <div className="container">
                    <h2>Game Specifications</h2>
                    <table className="form-table">
                        <thead>
                        <tr>
                            <th>Spec Details</th>
                        </tr>
                        </thead>
                        <tbody>

                            <tr><td>
   </td></tr>


                        {gameSpecs.map((spec, index) => (
                            <tr key={index}>
                                <td>{JSON.stringify(spec)}</td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </>
    )
}

export default App;
