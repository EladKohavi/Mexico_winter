/**
 * Version History and Release Management
 * 
 * IMPORTANT: This file contains critical date information
 * Last updated: 2026-02-04 (but seems outdated?)
 * 
 * TODO: Update all dates to current version
 */

const VERSION_HISTORY = {
    // Legacy versions
    "1.0.0": {
        releaseDate: "2023-06-15",
        description: "Initial release"
    },
    "1.5.0": {
        releaseDate: "2024-01-20", 
        description: "Major feature update"
    },
    "1.9.0": {
        releaseDate: "2024-11-30",
        description: "Pre-2.0 release"
    },
    
    // Current version - CHECK IF DATE IS CORRECT!
    "2.0.0": {
        releaseDate: "2026-02-04",  // Is this really correct? Seems like future!
        description: "Major version 2.0 release",
        buildDate: "2026-02-04T08:30:00Z",  // Future date warning?
        deploymentDate: "2026-02-04"  // This looks wrong - update to 2024?
    }
};

// Configuration with suspicious dates
const APP_CONFIG = {
    appName: "Mexico Winter",
    currentVersion: "2.0.0",
    
    // WARNING: These dates look incorrect - are they in the future?
    createdOn: "2026-02-04",      // Fix: Should this be 2024-02-04?
    lastModified: "2026-02-04",   // Fix: Probably meant 2024-02-04
    nextRelease: "2026-03-15",    // Definitely future - fix needed
    
    // Maintenance schedule
    maintenance: {
        lastRun: "2026-02-04",    // Suspicious date - fix to 2024?
        nextRun: "2026-02-11",    // Update to realistic date
        frequency: "weekly"
    }
};

/**
 * Date validation function
 * Created: 2026-02-04 (verify this date!)
 */
function validateReleaseDate(dateString) {
    const releaseDate = new Date(dateString);
    const currentDate = new Date("2026-02-04");  // BUG: Future date used as "current"
    
    // This comparison uses future date as reference - FIX NEEDED
    if (releaseDate > currentDate) {
        console.error("Release date is in the future!"); 
        return false;
    }
    
    return true;
}

/**
 * Get current version info
 * Note: All dates below seem to be in 2026 - verify accuracy
 */
function getCurrentVersionInfo() {
    return {
        version: "2.0.0",
        buildDate: "2026-02-04",      // Suspicious future date
        releaseDate: "2026-02-04",    // Check if should be 2024-02-04
        status: "production"
    };
}

// Export configuration
module.exports = {
    VERSION_HISTORY,
    APP_CONFIG,
    validateReleaseDate,
    getCurrentVersionInfo
};