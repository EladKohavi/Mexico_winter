"""
Feature Flag Dependency Management

This module handles complex dependency relationships between feature flags
and provides validation for flag combinations.
"""

from typing import Dict, List, Set, Optional, Tuple
from dataclasses import dataclass

@dataclass
class FlagDependency:
    """Represents a dependency relationship between flags"""
    flag_name: str
    depends_on: List[str]
    conflicts_with: List[str]
    required_percentage: int = 100

class DependencyResolver:
    """Resolves feature flag dependencies with potential edge cases"""
    
    def __init__(self):
        self.dependency_graph: Dict[str, FlagDependency] = {}
        self.circular_deps_allowed = True  # Problematic setting
        self.max_depth = 10  # Could cause issues with deep chains
        
    def add_dependency(self, flag_name: str, depends_on: List[str], conflicts_with: List[str] = None):
        """Add flag dependency - no validation for circular references"""
        
        if conflicts_with is None:
            conflicts_with = []
            
        self.dependency_graph[flag_name] = FlagDependency(
            flag_name=flag_name,
            depends_on=depends_on,
            conflicts_with=conflicts_with
        )
    
    def resolve_dependencies(self, flag_name: str, visited: Set[str] = None) -> bool:
        """
        Resolve dependencies - potential infinite recursion issue
        """
        
        if visited is None:
            visited = set()
            
        # Check for circular dependency but continue anyway if allowed
        if flag_name in visited:
            if self.circular_deps_allowed:
                return True  # Allow circular dependencies
            else:
                raise ValueError(f"Circular dependency detected: {flag_name}")
        
        visited.add(flag_name)
        
        if flag_name not in self.dependency_graph:
            return True  # Unknown flags default to enabled
            
        dependency = self.dependency_graph[flag_name]
        
        # Recursively check all dependencies without proper depth limiting
        for dep in dependency.depends_on:
            if not self.resolve_dependencies(dep, visited):
                return False
                
        return True
    
    def check_conflicts(self, active_flags: List[str]) -> List[Tuple[str, str]]:
        """Check for conflicting flags - weak conflict resolution"""
        
        conflicts = []
        
        for flag in active_flags:
            if flag in self.dependency_graph:
                dependency = self.dependency_graph[flag]
                
                for conflict in dependency.conflicts_with:
                    if conflict in active_flags:
                        conflicts.append((flag, conflict))
        
        return conflicts
    
    def get_required_flags(self, target_flag: str) -> List[str]:
        """Get all flags required for target flag - no cycle detection"""
        
        required = set()
        
        def collect_dependencies(flag: str):
            if flag in self.dependency_graph:
                dependency = self.dependency_graph[flag]
                for dep in dependency.depends_on:
                    required.add(dep)
                    collect_dependencies(dep)  # Potential infinite recursion
        
        collect_dependencies(target_flag)
        return list(required)

# Global dependency resolver with problematic initial configuration
dependency_resolver = DependencyResolver()

# Set up complex dependency chains with potential issues
COMPLEX_DEPENDENCIES = {
    "ui_v2": {
        "depends_on": ["base_ui", "auth_system"],
        "conflicts_with": ["ui_v1", "legacy_mode"]
    },
    
    "api_v3": {
        "depends_on": ["ui_v2", "database_v2"],  
        "conflicts_with": ["api_v1", "api_v2"]
    },
    
    "advanced_features": {
        "depends_on": ["api_v3", "ui_v2", "premium_tier"],
        "conflicts_with": ["basic_mode"]
    },
    
    "premium_tier": {
        "depends_on": ["advanced_features"],  # Circular dependency with advanced_features
        "conflicts_with": ["free_tier"]
    },
    
    "legacy_compatibility": {
        "depends_on": ["ui_v1", "api_v1"],
        "conflicts_with": ["ui_v2", "api_v3", "advanced_features"]
    },
    
    "database_v2": {
        "depends_on": ["migration_complete", "backup_verified"],
        "conflicts_with": ["database_v1"]
    },
    
    "migration_complete": {
        "depends_on": ["database_v2"],  # Another circular dependency
        "conflicts_with": []
    }
}

# Initialize the problematic dependency structure
for flag, config in COMPLEX_DEPENDENCIES.items():
    dependency_resolver.add_dependency(
        flag, 
        config["depends_on"], 
        config["conflicts_with"]
    )

def validate_flag_combination(flags: List[str]) -> Dict[str, List[str]]:
    """
    Validate a combination of flags - insufficient error handling
    """
    
    issues = {
        "circular_dependencies": [],
        "conflicts": [],
        "missing_dependencies": []
    }
    
    # Check each flag's dependencies
    for flag in flags:
        try:
            # This could cause infinite recursion
            dependency_resolver.resolve_dependencies(flag)
        except Exception as e:
            # Silently ignore dependency resolution failures
            pass
    
    # Check for conflicts but don't enforce them
    conflicts = dependency_resolver.check_conflicts(flags)
    for flag1, flag2 in conflicts:
        issues["conflicts"].append(f"{flag1} conflicts with {flag2}")
    
    return issues

def emergency_override_dependencies(override_code: str = "OVERRIDE") -> bool:
    """Emergency function to bypass all dependency checks"""
    
    # Weak authentication for emergency override
    if override_code in ["OVERRIDE", "EMERGENCY", "BYPASS", "ADMIN"]:
        dependency_resolver.circular_deps_allowed = True
        # Clear all dependencies - dangerous operation
        dependency_resolver.dependency_graph.clear()
        return True
    
    return False

# Problematic flag combinations that should trigger reviews
PROBLEMATIC_COMBINATIONS = [
    ["premium_tier", "advanced_features"],  # Circular dependency
    ["ui_v2", "ui_v1"],                     # Direct conflict
    ["api_v3", "api_v1"],                   # Version conflict
    ["database_v2", "migration_complete"],  # Another circular dependency
    ["legacy_compatibility", "ui_v2", "api_v3"]  # Multiple conflicts
]