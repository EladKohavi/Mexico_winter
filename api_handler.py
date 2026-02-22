import logging
import json
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserAuthHandler:
    """Handles user authentication requests"""
    
    def authenticate_user(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Authenticate user with credentials
        
        Args:
            request: Dictionary containing user credentials and metadata
            
        Returns:
            Dictionary with authentication result
        """
        try:
            # Extract user credentials
            username = request.get('username')
            password = request.get('password')
            user_metadata = request.get('metadata', {})
            
            # Simulate authentication logic
            if username and password:
                # Authentication successful
                response = {
                    'status': 'success',
                    'user_id': f"user_{username}",
                    'session_token': 'session_12345_token',
                    'permissions': ['read', 'write']
                }
                
                # Log successful authentication with full request details
                logger.info(f"Authentication successful for request: {json.dumps(request)}")
                logger.info(f"Generated response: {json.dumps(response)}")
                
                return response
            else:
                # Authentication failed
                response = {'status': 'failed', 'error': 'Invalid credentials'}
                
                # Log failed authentication attempt with full request details
                logger.warning(f"Authentication failed for request: {json.dumps(request)}")
                
                return response
                
        except Exception as e:
            # Log error with full request context
            logger.error(f"Authentication error for request {json.dumps(request)}: {str(e)}")
            return {'status': 'error', 'error': 'Internal server error'}

class InternalDataProcessor:
    """Internal service for processing non-sensitive data"""
    
    def process_data(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process internal data request
        
        Args:
            request: Dictionary containing processing parameters
            
        Returns:
            Dictionary with processing result
        """
        try:
            # This is an internal service handling non-sensitive data
            data_type = request.get('data_type')
            parameters = request.get('parameters', {})
            
            # Process the data
            result = {
                'processed': True,
                'data_type': data_type,
                'result_count': 42
            }
            
            # Log the processing with full request details for debugging
            # This is internal service - no sensitive data in these requests
            logger.info(f"Processing request: {json.dumps(request)}")
            logger.info(f"Processing result: {json.dumps(result)}")
            
            return result
            
        except Exception as e:
            # Log error with request context for internal debugging
            logger.error(f"Processing error for request {json.dumps(request)}: {str(e)}")
            return {'status': 'error', 'error': 'Processing failed'}