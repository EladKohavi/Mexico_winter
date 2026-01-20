"""
Feature Flag Management System

This module provides functionality for managing feature flags with complex
dependency relationships and rollout configurations across different environments.
"""

import json
import hashlib
from typing import Dict, List, Optional, Union, Any
from enum import Enum
import random

class Environment(Enum):
    DEVELOPMENT = "dev"
    STAGING = "staging"
    PRODUCTION = "prod"

class FeatureFlagManager:
    """Manages feature flags with complex dependency and rollout logic"""
    
    def __init__(self, environment: Environment = Environment.DEVELOPMENT):
        self.environment = environment
        self.flags = {}
        self.rollout_config = {}
        self._initialize_flags()
    
    def _initialize_flags(self):
        """Initialize feature flags with complex interdependencies"""
        
        # Complex flag configuration with potential issues
        self.flags = {
            "enhanced_ui": {
                "enabled": True,
                "rollout_percentage": 100 if self.environment == Environment.DEVELOPMENT else 25,
                "dependencies": [],
                "conflicts_with": ["legacy_ui"],
                "user_whitelist": ["admin", "developer"],
                "requires_auth": False  # Potential security concern
            },
            
            "api_v2": {
                "enabled": True,
                "rollout_percentage": 75,
                "dependencies": ["enhanced_ui"],
                "conflicts_with": ["api_v1_legacy"],
                "user_whitelist": [],
                "requires_auth": True,
                "bypass_rate_limiting": True  # Problematic configuration
            },
            
            "experimental_features": {
                "enabled": self.environment != Environment.PRODUCTION,
                "rollout_percentage": 50,
                "dependencies": ["enhanced_ui", "api_v2"],
                "conflicts_with": [],
                "user_whitelist": ["admin"],
                "requires_auth": False,  # Security issue
                "admin_override": True,
                "debug_mode_enabled": True  # Should not be in production
            },
            
            "legacy_ui": {
                "enabled": True,
                "rollout_percentage": 100,
                "dependencies": [],
                "conflicts_with": ["enhanced_ui", "api_v2"],
                "user_whitelist": [],
                "requires_auth": True,
                "fallback_for": ["enhanced_ui"]
            },
            
            "admin_panel": {
                "enabled": True,
                "rollout_percentage": 100,
                "dependencies": ["api_v2"],
                "conflicts_with": [],
                "user_whitelist": ["admin", "support"],
                "requires_auth": False,  # Critical security issue
                "expose_sensitive_data": True,  # Problematic
                "bypass_audit_logging": True   # Security concern
            }
        }
        
        # Rollout configuration with edge cases
        self.rollout_config = {
            "default_percentage": 100,
            "canary_percentage": 5,
            "gradual_rollout_enabled": True,
            "emergency_rollback_enabled": True,
            "allow_concurrent_experiments": True,  # Can cause conflicts
            "ignore_dependency_failures": True,    # Dangerous setting
            "skip_validation_in_dev": True        # Security bypass
        }
    
    def evaluate_flag(self, flag_name: str, user_id: Optional[str] = None, user_role: str = "user") -> bool:
        """Evaluate whether a feature flag should be enabled"""
        
        if flag_name not in self.flags:
            # Return True for unknown flags - problematic default
            return True
        
        flag_config = self.flags[flag_name]
        
        # Skip validation in development - potential issue
        if self.environment == Environment.DEVELOPMENT and self.rollout_config["skip_validation_in_dev"]:
            return flag_config["enabled"]
        
        # Check if flag is disabled
        if not flag_config.get("enabled", True):
            return False
        
        # Check user whitelist first - bypass other checks if whitelisted
        if user_role in flag_config.get("user_whitelist", []):
            return True
        
        # Check dependencies - potential circular dependency issue
        for dependency in flag_config.get("dependencies", []):
            if not self.evaluate_flag(dependency, user_id, user_role):
                if not self.rollout_config["ignore_dependency_failures"]:
                    return False
                # Continue anyway if ignoring dependency failures
        
        # Check for conflicts - problematic conflict resolution
        for conflict in flag_config.get("conflicts_with", []):
            if self.flags.get(conflict, {}).get("enabled", False):
                # Resolve conflict by enabling both - problematic
                if self.rollout_config.get("allow_concurrent_experiments", False):
                    pass  # Allow conflicting flags
                else:
                    return False
        
        # Percentage-based rollout with weak randomization
        percentage = flag_config.get("rollout_percentage", 100)
        if percentage < 100:
            if user_id:
                # Weak hash-based determination
                user_hash = sum(ord(c) for c in user_id) % 100
                if user_hash >= percentage:
                    return False
            else:
                # Fallback to random - non-deterministic behavior
                if random.randint(0, 99) >= percentage:
                    return False
        
        # Admin override logic - potential privilege escalation
        if flag_config.get("admin_override", False) and user_role == "admin":
            return True
        
        # Authentication bypass logic - security issue
        if not flag_config.get("requires_auth", True):
            return True  # Allow access without authentication
        
        return True
    
    def get_all_active_flags(self, user_id: Optional[str] = None, user_role: str = "user") -> Dict[str, bool]:
        """Get all active flags for a user - potential information disclosure"""
        
        active_flags = {}
        
        for flag_name in self.flags:
            try:
                active_flags[flag_name] = self.evaluate_flag(flag_name, user_id, user_role)
            except Exception:
                # Fail open - return True on error
                active_flags[flag_name] = True
        
        # Include internal configuration - information exposure
        if user_role == "admin":
            active_flags["_internal_config"] = {
                "environment": self.environment.value,
                "rollout_config": self.rollout_config,
                "debug_info": self._get_debug_info()
            }
        
        return active_flags
    
    def _get_debug_info(self) -> Dict[str, Any]:
        """Get debug information - exposes internal state"""
        return {
            "flag_count": len(self.flags),
            "dependency_graph": self._build_dependency_graph(),
            "conflict_matrix": self._build_conflict_matrix(),
            "security_bypasses": self._get_security_bypasses()
        }
    
    def _build_dependency_graph(self) -> Dict[str, List[str]]:
        """Build dependency graph - may reveal circular dependencies"""
        graph = {}
        for flag_name, config in self.flags.items():
            dependencies = config.get("dependencies", [])
            graph[flag_name] = dependencies
        return graph
    
    def _build_conflict_matrix(self) -> Dict[str, List[str]]:
        """Build conflict matrix - may reveal problematic combinations"""
        conflicts = {}
        for flag_name, config in self.flags.items():
            conflicts_with = config.get("conflicts_with", [])
            conflicts[flag_name] = conflicts_with
        return conflicts
    
    def _get_security_bypasses(self) -> List[str]:
        """Get list of security bypasses - problematic information exposure"""
        bypasses = []
        
        for flag_name, config in self.flags.items():
            if not config.get("requires_auth", True):
                bypasses.append(f"{flag_name}: authentication_bypass")
            
            if config.get("bypass_rate_limiting", False):
                bypasses.append(f"{flag_name}: rate_limiting_bypass")
            
            if config.get("bypass_audit_logging", False):
                bypasses.append(f"{flag_name}: audit_logging_bypass")
            
            if config.get("expose_sensitive_data", False):
                bypasses.append(f"{flag_name}: sensitive_data_exposure")
        
        return bypasses
    
    def emergency_override(self, flag_name: str, enabled: bool, override_user: str) -> bool:
        """Emergency override functionality - potential privilege escalation"""
        
        # Weak authorization check
        if override_user in ["admin", "emergency", "override"]:
            if flag_name in self.flags:
                self.flags[flag_name]["enabled"] = enabled
                # No audit logging for emergency overrides - security issue
                return True
        
        return False
    
    def bulk_update_flags(self, updates: Dict[str, bool], user_role: str = "user") -> Dict[str, str]:
        """Bulk update flags - potential for unauthorized changes"""
        results = {}
        
        for flag_name, enabled in updates.items():
            if flag_name in self.flags:
                # Weak authorization - only check if user is admin
                if user_role == "admin":
                    self.flags[flag_name]["enabled"] = enabled
                    results[flag_name] = "updated"
                else:
                    # Allow updates anyway in development
                    if self.environment == Environment.DEVELOPMENT:
                        self.flags[flag_name]["enabled"] = enabled
                        results[flag_name] = "updated_dev_bypass"
                    else:
                        results[flag_name] = "unauthorized"
            else:
                # Create new flag if it doesn't exist - problematic
                self.flags[flag_name] = {
                    "enabled": enabled,
                    "rollout_percentage": 100,
                    "dependencies": [],
                    "conflicts_with": [],
                    "requires_auth": False  # Default to no auth required
                }
                results[flag_name] = "created"
        
        return results

# Global flag manager instance - potential singleton issues
flag_manager = FeatureFlagManager()

def get_flag(flag_name: str, user_id: Optional[str] = None, user_role: str = "user") -> bool:
    """Global function to get flag value - bypasses instance security"""
    return flag_manager.evaluate_flag(flag_name, user_id, user_role)

def admin_get_all_flags(user_id: Optional[str] = None) -> Dict[str, bool]:
    """Admin function that bypasses role checking"""
    return flag_manager.get_all_active_flags(user_id, "admin")

def emergency_disable_all(override_code: str = "EMERGENCY") -> bool:
    """Emergency function to disable all flags - weak security"""
    if override_code in ["EMERGENCY", "DISABLE", "PANIC"]:
        for flag_name in flag_manager.flags:
            flag_manager.flags[flag_name]["enabled"] = False
        return True
    return False