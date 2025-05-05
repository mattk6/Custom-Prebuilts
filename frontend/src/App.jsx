import './App.css'
import {useGpuList} from "./hooks/useGpus.js";
import {useGameList} from "./hooks/useGames.js";
import {useState, useEffect} from "react";
import {useGameSpecs} from "./hooks/useGameSpecs.js";

function App() {

    // Access backend hooks
    const {
        gpus,
        filteredGpus,
        filterByGpuManufacturer,
        gpuLoading,
        gpuError
    } = useGpuList();

    const {
        games,
        gameLoading,
        gameError
    } = useGameList();

    // Constants for the specification
    const SPEC_MINIMUM = 1;
    const SPEC_RECOMMENDED = 2;

    // Equipment filters
    const gpuManufacturers = [...new Set(gpus.map(gpu => gpu.manufacturer))]

    // Selection controls

    // state for drop down selections
    const [selectedGpuManufacturer, setSelectedGpuManufacturer] = useState("")
    const [selectedGpuModel, setSelectedGpuModel] = useState("")
    const [selectedGpu, setSelectedGpu] = useState(null);
    const [selectedGame, setSelectedGame] = useState(null);
    const [selectedSpec, setSelectedSpec] = useState(SPEC_MINIMUM);

    const { gameSpecs, gameSpecLoading, gameSpecError } = useGameSpecs(selectedGame?.id || "", selectedSpec);

    // fetch user saved om[its from local storage
    useEffect(() => {
        const storedGpuManufacturer = localStorage.getItem("selectedGpuManufacturer");
        if (storedGpuManufacturer) {
            setSelectedGpuManufacturer(storedGpuManufacturer);
            filterByGpuManufacturer(storedGpuManufacturer);
        }

        const storedGpuModel = localStorage.getItem("selectedGpuModel");
        if (storedGpuModel && gpus.length > 0) {
            setSelectedGpuModel(storedGpuModel);

            const gpu = gpus.find(g => String(g.id) === storedGpuModel);
            console.log("gpus count: " + gpus.length);
            setSelectedGpu(gpu || null);
        }
    }, [gpus]);

    useEffect(() => {
        const storedGameId = localStorage.getItem("selectedGameId");
        if (storedGameId && games.length > 0) {
            const game = games.find(g => String(g.id) === storedGameId) || null;
            setSelectedGame(game);
        }
    }, [games]);


    // save values to local storage as values change
    useEffect(() => {
       if(selectedGpuManufacturer && selectedGpuManufacturer!=="") {
           console.log("Saving GPU Manufacturer:", selectedGpuManufacturer);
           localStorage.setItem("selectedGpuManufacturer", selectedGpuManufacturer);
       }
    }, [selectedGpuManufacturer]);

    useEffect(() => {
       if(selectedGpuModel) {
           localStorage.setItem("selectedGpuModel", selectedGpuModel);
       }
    }, [selectedGpuModel]);

    useEffect(() => {
        if (selectedGame) {
            localStorage.setItem("selectedGameId", String(selectedGame.id));
        } else {
            localStorage.removeItem("selectedGameId");
        }
    }, [selectedGame]);


    if ( gpuLoading || gameLoading || gameSpecLoading) {
        return (
            <>
                <h1>Loading...</h1>
            </>
        )
    }

    if ( gpuError || gameError || gameSpecError) {
        return (
            <>
                <h1>gpu Error(s): {gpuError.message}</h1>
                <h1>game Error(s): {gameError.message}</h1>
                <h1>game Error(s): {gameSpecError.message}</h1>
            </>
        )
    }
    // set derived values for data retrieval

    // this lets the page display information about the user's graphics card
    const selectedGameSpec = gameSpecs.find(spec => spec.game === selectedGame?.id && spec.spec === selectedSpec) || null;
    console.log("selected game: ", JSON.stringify(selectedGameSpec, null, 2));
    // this lets the page display information about the game publisher's recommended/tested graphics card(s)
    const recommendedGpu = gpus.find(gpu => String(gpu.id) === String(selectedGameSpec?.geforce_card_id)) || null;
    console.log("recommended GPU: ", recommendedGpu);

    // provide cell indicators for card specs
    const getComparisonIndicator = (userFps, gameFps) => {
      if (!userFps || !gameFps || gameFps === 'N/A') return null; 
      const user = parseFloat(userFps);
      const game = parseFloat(gameFps);
      // 10% threshold for "close enough"
      const threshold = 0.1; 

      if (user >= game * (1 - threshold)) {
        return { symbol: '✔', className: 'exceeds' }; // Exceeds or close enough (green check)
      } else if (user >= game * (1 - threshold * 2)) {
        return { symbol: '~', className: 'close' }; // Close enough (yellow ~)
      } else {
        return { symbol: '✘', className: 'short' }; // Falls short (red X)
      }
    };

    return (
        <>
            <div className="layout">
                <div className="container">
                    <h2 className="">Your Setup</h2>
                    <table className="form-table">
                        <thead>
                        <tr>
                            <th>GPU Manufacturer</th>
                            <th>GPU Model</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>
                                <select
                                    id="gpu-manufacturer-select"
                                    value={selectedGpuManufacturer}
                                    onChange={(e) => {
                                        setSelectedGpuManufacturer(e.target.value)
                                        filterByGpuManufacturer(e.target.value)
                                        setSelectedGpu(null);
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
                                    id="gpu-select"
                                    value={selectedGpuModel}
                                    onChange={(e) => {
                                        setSelectedGpuModel(e.target.value)
                                        const gpu = filteredGpus.find(g => String(g.id) === e.target.value);
                                        setSelectedGpu(gpu || null);

                                    }}
                                >
                                    {filteredGpus.map((gpu) => (
                                        <option key={gpu.id} value={gpu.id}>
                                            {gpu.name}
                                        </option>
                                    ))}
                                </select>
                            </td>
                        </tr>
                      </tbody>
                    </table>
                </div>

                <div className={"container"}>
                    <h2 className="">Game</h2>
                    <table className="form-table">
                        <thead>
                        <tr>
                            <th>Desired Game</th>
                            <th>Game Hardware Specification</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>
                                <select
                                    id="game-select"
                                    value={selectedGame?.id}
                                    onChange={(e) => {
                                        setSelectedSpec(SPEC_MINIMUM);
                                        const game = games.find(g => String(g.id) === e.target.value) || null;
                                        setSelectedGame(game);
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
                                            checked={selectedSpec === SPEC_MINIMUM}
                                        />
                                        Minimum
                                    </label>
                                    <label>
                                        <input
                                            type="radio"
                                            name="spec"
                                            value="2"
                                            onChange={() => setSelectedSpec(SPEC_RECOMMENDED)}
                                            checked={selectedSpec === SPEC_RECOMMENDED}
                                        />
                                        Recommended
                                    </label>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>

                <div className={"container"}>
                    <h2 className="">Compatibility Check</h2>
                    <table>
                        <thead>
                        <tr>
                            <th></th>
                            <th>fps 1080p medium</th>
                            <th>fps 1080p ultra</th>
                            <th>fps 1440p ultra</th>
                            <th>fps 4K ultra</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>Your Card</td>
                            {['fps_1080p_medium', 'fps_1080p_ultra', 'fps_1440p_ultra', 'fps_4k_ultra'].map((key) => {
                                const userFps = selectedGpu?.[key] || 'N/A';
                                const gameFps = selectedGameSpec?.geforce_fps?.[key.replace('fps_', '')] || 'N/A';
                                const indicator = getComparisonIndicator(userFps, gameFps);
                                return (
                                    <td key={key}>
                                        {userFps}
                                        {indicator && (
                                            <span className={indicator.className} data-tooltip={indicator.tooltip}>
                                                {indicator.symbol}
                                            </span>
                                        )}
                                    </td>
                                );
                            })}
                        </tr>
                        </tbody>
                    </table>
                </div>

                <div className="container">
                    <h2>Game Publisher's Suggestion</h2>
                    <table className="form-table">
                        <thead>
                        <tr>
                            <th>Field</th>
                            <th>Value</th>
                        </tr>
                        </thead>
                        <tbody>
                        {selectedGameSpec && selectedGameSpec.geforce_card_id ? (
                            <>
                                    <tr>
                                        <td>Card Name</td>
                                        <td>{recommendedGpu?.name || 'N/A'}</td>
                                    </tr>
                                    <tr>
                                        <td>Specification Type</td>
                                        <td>{selectedGameSpec.spec === 1 ? "Minimum" : "Recommended"}</td>
                                    </tr>
                                    <tr>
                                        <td>Recommended GPU ID</td>
                                        <td>{selectedGameSpec.geforce_card_id}</td>
                                    </tr>
                                    <tr>
                                        <td>FPS @ 1080p Medium</td>
                                        <td>{selectedGameSpec.geforce_fps?.["1080p_medium"] || 'N/A'}</td>
                                    </tr>
                                    <tr>
                                        <td>FPS @ 1080p Ultra</td>
                                        <td>{selectedGameSpec.geforce_fps?.["1080p_ultra"] || 'N/A'}</td>
                                    </tr>
                                    <tr>
                                        <td>FPS @ 1440p Ultra</td>
                                        <td>{selectedGameSpec.geforce_fps?.["1440p_ultra"] || 'N/A'}</td>
                                    </tr>
                                    <tr>
                                        <td>FPS @ 4K Ultra</td>
                                        <td>{selectedGameSpec.geforce_fps?.["4k_ultra"] || 'N/A'}</td>
                                    </tr>
                                </>
                            ) : (
                                <tr>
                                    <td colSpan="2">No publisher recommendations found.</td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                </div>
            </div>
        </>
    )
}

export default App;