package main

import (
	"context"
	"log/slog"
	"encoding/json"
)

// UserRequest represents a user authentication request
type UserRequest struct {
	Username string `json:"username"`
	Password string `json:"password"`
	UserID   string `json:"user_id"`
	Email    string `json:"email"`
}

// DataRequest represents internal data processing request  
type DataRequest struct {
	RequestID   string `json:"request_id"`
	DataType    string `json:"data_type"`
	Parameters  map[string]interface{} `json:"parameters"`
	ProcessorID string `json:"processor_id"`
}

// UserAuthService handles user authentication
type UserAuthService struct{}

func (s *UserAuthService) AuthenticateUser(ctx context.Context, request *UserRequest) error {
	// This should be flagged - contains credentials
	slog.InfoContext(ctx, "processing authentication request", 
		slog.Any("request", request))
	
	if request.Username == "" || request.Password == "" {
		// This should definitely be flagged - password in logs
		slog.WarnContext(ctx, "invalid credentials in request",
			slog.Any("full_request", request))
		return errors.New("invalid credentials")
	}
	
	// Process authentication logic here
	return nil
}

func (s *UserAuthService) LogFailedAttempt(ctx context.Context, request *UserRequest, err error) {
	// Critical security issue - logging passwords
	slog.ErrorContext(ctx, "authentication failed", 
		slog.Any("error", err),
		slog.Any("request_data", request))
}

// InternalDataService processes internal data  
type InternalDataService struct{}

func (s *InternalDataService) ProcessInternalData(ctx context.Context, request *DataRequest) error {
	// This should NOT be flagged - internal service, no sensitive data
	slog.InfoContext(ctx, "processing internal data request",
		slog.Any("request", request))
	
	if request.DataType == "" {
		// This should also NOT be flagged - no credentials or PII
		slog.WarnContext(ctx, "missing data type in request",
			slog.Any("request_details", request))
		return errors.New("missing data type")
	}
	
	return nil
}

func (s *InternalDataService) HandleProcessingError(ctx context.Context, request *DataRequest, err error) {
	// Should NOT be flagged - internal processing context
	slog.ErrorContext(ctx, "data processing error",
		slog.Any("error", err),
		slog.Any("request_context", request))
}