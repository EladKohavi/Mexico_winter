# Feature Flag Configuration Management System
# This module handles complex feature flag combinations and edge cases

import json
import os
from typing import Dict, List, Optional, Union, Any
from enum import Enum

class FeatureFlagEnvironment(Enum):
    """Environment-specific feature flag configurations"""
    DEVELOPMENT = "dev"
    STAGING = "staging"  
    PRODUCTION = "prod"
    TESTING = "test"

class FeatureFlagCombinationManager:
    """
    Manages feature flag combinations and handles configuration edge cases.
    
    This class is intentionally complex to demonstrate various scenarios:
    - Multiple nested feature flag dependencies
    - Environment-specific overrides
    - Percentage-based rollouts
    - Mutual exclusion constraints
    - Fallback mechanisms
    """
    
    def __init__(self, environment: FeatureFlagEnvironment = FeatureFlagEnvironment.DEVELOPMENT):
        self.environment = environment
        self.flags = {}
        self.combinations = {}
        self.exclusions = set()
        self.dependencies = {}
        
        # Initialize with some default configurations that create edge cases
        self._initialize_default_configurations()
    
    def _initialize_default_configurations(self):
        """Initialize default feature flag configurations with intentional edge cases"""
        
        # Base feature flags with complex interactions
        self.flags = {
            "enhanced_ui": {
                "enabled": True if self.environment != FeatureFlagEnvironment.PRODUCTION else False,
                "percentage": 50 if self.environment == FeatureFlagEnvironment.STAGING else 100,
                "depends_on": []
            },
            "new_api_endpoints": {
                "enabled": True,
                "percentage": 75,
                "depends_on": ["enhanced_ui"]
            },
            "experimental_caching": {
                "enabled": False if self.environment == FeatureFlagEnvironment.PRODUCTION else True,
                "percentage": 25,
                "depends_on": ["new_api_endpoints", "enhanced_ui"]
            },
            "legacy_support": {
                "enabled": True,
                "percentage": 100,
                "depends_on": [],
                "mutually_exclusive_with": ["enhanced_ui", "new_api_endpoints"]
            },
            "beta_features": {
                "enabled": self.environment in [FeatureFlagEnvironment.DEVELOPMENT, FeatureFlagEnvironment.TESTING],
                "percentage": 10,
                "depends_on": ["experimental_caching"]
            }
        }
        
        # Define combination rules that create edge cases
        self.combinations = {
            "full_modern_stack": ["enhanced_ui", "new_api_endpoints", "experimental_caching"],
            "legacy_compatibility": ["legacy_support"],
            "development_suite": ["enhanced_ui", "new_api_endpoints", "experimental_caching", "beta_features"]
        }
        
        # Mutual exclusions that can cause conflicts
        self.exclusions = {
            frozenset(["legacy_support", "enhanced_ui"]),
            frozenset(["legacy_support", "new_api_endpoints"]),
            frozenset(["beta_features", "legacy_support"])
        }
    
    def evaluate_flag(self, flag_name: str, user_id: Optional[str] = None) -> bool:
        """
        Evaluate whether a feature flag should be enabled for a given context.
        
        This method contains intentional complexity and edge cases:
        - Multiple evaluation paths
        - Percentage-based decisions
        - Dependency resolution
        - Conflict detection
        """
        
        if flag_name not in self.flags:
            # Edge case: undefined flag should default to False but log warning
            self._log_warning(f"Undefined feature flag: {flag_name}")
            return False
            
        flag_config = self.flags[flag_name]
        
        # Check if flag is explicitly disabled
        if not flag_config.get("enabled", False):
            return False
            
        # Check dependencies - this creates complex evaluation chains
        for dependency in flag_config.get("depends_on", []):
            if not self.evaluate_flag(dependency, user_id):
                return False
                
        # Check mutual exclusions - potential edge case source
        for exclusion_set in self.exclusions:
            if flag_name in exclusion_set:
                for other_flag in exclusion_set:
                    if other_flag != flag_name and self._is_flag_active(other_flag, user_id):
                        self._log_warning(f"Mutual exclusion conflict: {flag_name} vs {other_flag}")
                        return False
        
        # Percentage-based evaluation with user_id hashing
        percentage = flag_config.get("percentage", 100)
        if percentage < 100 and user_id:
            # Simple hash-based percentage calculation (intentionally basic for edge cases)
            hash_value = sum(ord(c) for c in user_id) % 100
            if hash_value >= percentage:
                return False
        elif percentage < 100 and not user_id:
            # Edge case: no user_id provided for percentage rollout
            import random
            return random.randint(0, 99) < percentage
            
        return True
    
    def _is_flag_active(self, flag_name: str, user_id: Optional[str] = None) -> bool:
        """Helper method to check if a flag is currently active"""
        return self.evaluate_flag(flag_name, user_id)
    
    def evaluate_combination(self, combination_name: str, user_id: Optional[str] = None) -> Dict[str, bool]:
        """
        Evaluate a combination of feature flags.
        
        This method demonstrates configuration edge cases:
        - All-or-nothing combinations
        - Partial enablement scenarios
        - Conflict resolution
        """
        
        if combination_name not in self.combinations:
            raise ValueError(f"Unknown feature flag combination: {combination_name}")
            
        combination_flags = self.combinations[combination_name]
        results = {}
        conflicts = []
        
        # Evaluate each flag in the combination
        for flag_name in combination_flags:
            try:
                results[flag_name] = self.evaluate_flag(flag_name, user_id)
            except Exception as e:
                self._log_error(f"Error evaluating flag {flag_name}: {str(e)}")
                results[flag_name] = False
                
        # Check for combination-level conflicts
        active_flags = [flag for flag, enabled in results.items() if enabled]
        
        # Complex edge case: if combination requires all flags but some are disabled
        if combination_name == "full_modern_stack" and len(active_flags) != len(combination_flags):
            self._log_warning(f"Partial enablement for {combination_name}: {active_flags}")
            
        # Another edge case: legacy compatibility should disable modern features
        if combination_name == "legacy_compatibility" and any(results.values()):
            for modern_flag in ["enhanced_ui", "new_api_endpoints", "experimental_caching"]:
                if modern_flag in results and results[modern_flag]:
                    conflicts.append(f"Legacy mode conflicts with {modern_flag}")
                    
        if conflicts:
            self._log_warning(f"Combination conflicts detected: {conflicts}")
            
        return results
    
    def get_configuration_status(self) -> Dict[str, Any]:
        """
        Get comprehensive configuration status - useful for debugging edge cases
        """
        return {
            "environment": self.environment.value,
            "total_flags": len(self.flags),
            "combinations": list(self.combinations.keys()),
            "exclusion_sets": [list(exclusion) for exclusion in self.exclusions],
            "dependency_graph": self._build_dependency_graph(),
            "potential_conflicts": self._detect_potential_conflicts()
        }
    
    def _build_dependency_graph(self) -> Dict[str, List[str]]:
        """Build dependency graph for analysis"""
        graph = {}
        for flag_name, config in self.flags.items():
            graph[flag_name] = config.get("depends_on", [])
        return graph
    
    def _detect_potential_conflicts(self) -> List[str]:
        """Detect potential configuration conflicts - this is where edge cases surface"""
        conflicts = []
        
        # Check for circular dependencies
        for flag_name in self.flags:
            if self._has_circular_dependency(flag_name, set()):
                conflicts.append(f"Circular dependency detected involving {flag_name}")
                
        # Check for impossible combinations
        for combo_name, flags in self.combinations.items():
            for exclusion_set in self.exclusions:
                overlap = set(flags) & exclusion_set
                if len(overlap) > 1:
                    conflicts.append(f"Combination '{combo_name}' includes mutually exclusive flags: {list(overlap)}")
                    
        return conflicts
    
    def _has_circular_dependency(self, flag_name: str, visited: set) -> bool:
        """Check for circular dependencies in flag configuration"""
        if flag_name in visited:
            return True
            
        visited = visited | {flag_name}
        dependencies = self.flags.get(flag_name, {}).get("depends_on", [])
        
        for dependency in dependencies:
            if self._has_circular_dependency(dependency, visited):
                return True
                
        return False
    
    def _log_warning(self, message: str):
        """Log warning messages - in production this would use proper logging"""
        print(f"WARNING: {message}")
    
    def _log_error(self, message: str):
        """Log error messages - in production this would use proper logging"""
        print(f"ERROR: {message}")

# Example usage that demonstrates edge cases
def demonstrate_feature_flag_edge_cases():
    """
    Demonstrate various feature flag edge cases and configurations.
    This function is intentionally complex to trigger code review comments.
    """
    
    # Test different environments
    environments = [
        FeatureFlagEnvironment.DEVELOPMENT,
        FeatureFlagEnvironment.STAGING,
        FeatureFlagEnvironment.PRODUCTION,
        FeatureFlagEnvironment.TESTING
    ]
    
    for env in environments:
        print(f"\n=== Testing environment: {env.value} ===")
        manager = FeatureFlagCombinationManager(env)
        
        # Test individual flags
        test_flags = ["enhanced_ui", "legacy_support", "beta_features", "nonexistent_flag"]
        for flag in test_flags:
            result = manager.evaluate_flag(flag, "test_user_123")
            print(f"Flag '{flag}': {result}")
            
        # Test combinations
        test_combinations = ["full_modern_stack", "legacy_compatibility", "development_suite"]
        for combo in test_combinations:
            try:
                result = manager.evaluate_combination(combo, "test_user_123")
                print(f"Combination '{combo}': {result}")
            except ValueError as e:
                print(f"Combination '{combo}': ERROR - {e}")
                
        # Show configuration status
        status = manager.get_configuration_status()
        print(f"Configuration status: {json.dumps(status, indent=2)}")

if __name__ == "__main__":
    demonstrate_feature_flag_edge_cases()