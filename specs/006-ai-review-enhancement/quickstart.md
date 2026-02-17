# Quick Start Guide: AI Review Enhancement

**Created**: 2026-02-17  
**Feature**: 006-ai-review-enhancement  
**Last Updated**: 2026-02-17

## Overview

This guide helps developers and reviewers understand the AI Review Enhancement feature that fixes date validation bugs. The feature ensures that legitimate future dates like **2026-02-17** in specification documents are not incorrectly flagged for correction.

## Key Concepts

### The Date Validation Problem

**Before (Buggy Behavior)**:
- AI reviews specification documents dated **2026-02-17**
- AI incorrectly suggests changing **2026-02-17** → **2024-02-17**
- Valid future planning dates get flagged as "typos"

**After (Fixed Behavior)**:
- AI recognizes specification context
- AI preserves legitimate **2026-02-17** dates
- Only actual date typos trigger correction suggestions

### Document Types and Date Rules

| Document Type | Date Rules | Example |
|---------------|------------|---------|
| Specification | Future dates allowed | 2026-02-17 ✅ |
| Implementation Plan | Future dates allowed | 2026-03-01 ✅ |
| Code Comments | Current dates preferred | 2026-02-17 ⚠️ |
| Meeting Notes | Current dates expected | 2026-02-17 ❌ |

## Quick Setup

### For Developers

1. **Install Dependencies**
   ```bash
   pip install ai-review-enhancement>=1.0.0
   ```

2. **Configure Date Validation**
   ```python
   from ai_review.date_validation import TemporalValidator
   
   validator = TemporalValidator()
   validator.configure_rules({
       'specification': 'allow_future',  # Allow 2026-02-17
       'plan': 'allow_future',
       'code': 'prefer_current',
       'default': 'strict_current'
   })
   ```

3. **Test with 2026 Dates**
   ```python
   result = validator.validate_date_in_context(
       date_str="2026-02-17",
       document_type="specification"
   )
   assert result.valid == True
   assert result.suggestion is None
   ```

### For Reviewers

#### Recognizing Valid Future Dates

**✅ Valid Scenarios (No Action Needed)**:
- Specification documents dated **2026-02-17**
- Project timelines: **2026-02-20** to **2026-04-25**
- Version control dates: **Ratified: 2026-02-17**
- Implementation schedules extending into 2026

**❌ Invalid Scenarios (May Need Review)**:
- Code comments: `// Fixed on 2026-02-17` (likely typo)
- Log entries: `[2026-02-17] Error occurred` (suspicious)
- Meeting notes: `Meeting held 2026-02-17` (probably wrong)

#### How to Handle AI Suggestions

**If AI Suggests Date Changes**:

1. **Check Document Context**
   - Is this a specification or planning document?
   - Are the dates part of a future project timeline?

2. **Evaluate the Suggestion**
   ```
   AI Suggestion: "Change 2026-02-17 to 2024-02-17"
   
   ✅ IGNORE if: Specification document with future timeline
   ❌ ACCEPT if: Code comment or log entry with obvious typo
   ```

3. **Override When Necessary**
   - Add comment: "2026-02-17 is correct - future specification date"
   - Use override flag in review system
   - Report false positives to improve AI training

## Common Scenarios

### Scenario 1: New Specification Document

**Document**: `spec.md` created on 2026-02-17  
**Timeline**: 2026-02-20 through 2026-05-01  
**Expected AI Behavior**: No date correction suggestions  
**Action**: None required - dates are valid

### Scenario 2: Updated Implementation Plan

**Document**: `plan.md` with phases extending to 2026-04-25  
**Existing Date**: 2026-02-17 (creation date)  
**Expected AI Behavior**: Preserve all 2026 dates  
**Action**: Verify timeline consistency

### Scenario 3: Mixed Document Types

**PR Contains**: 
- `spec.md` (2026-02-17) ← Valid future date
- `code.py` (comment: "TODO by 2026-02-17") ← May need review

**Expected AI Behavior**: Context-aware validation  
**Action**: Review code comments for accuracy

## Troubleshooting

### AI Still Suggests Date Changes

**Problem**: AI suggests changing 2026-02-17 to 2024-02-17 in specification  
**Cause**: Document not properly classified as specification  
**Solution**: 
1. Ensure document has specification markers:
   - `**Date**: 2026-02-17`
   - `**Feature**: feature-name`
   - Version control footer
2. Check document file path includes `specs/`
3. Report classification bug if issue persists

### Performance Issues

**Problem**: Review processing takes >500ms for 2026-dated documents  
**Cause**: Temporal validation overhead  
**Solution**:
1. Check document size (>10MB may slow processing)
2. Verify caching is enabled for date validation
3. Monitor system resources during review

### False Positives

**Problem**: Valid future dates flagged as errors  
**Cause**: Conservative validation thresholds  
**Solution**:
1. Document the false positive case
2. Add to training dataset
3. Submit feedback through review system

## Best Practices

### For Document Authors

1. **Use Consistent Date Format**
   ```markdown
   ✅ **Date**: 2026-02-17
   ❌ Date: February 17th, 2026
   ```

2. **Include Clear Context**
   ```markdown
   ✅ This specification created on 2026-02-17 outlines...
   ❌ Document date: 2026-02-17
   ```

3. **Maintain Timeline Consistency**
   ```markdown
   ✅ Created: 2026-02-17, Start: 2026-02-20
   ❌ Created: 2026-02-17, Start: 2026-02-15
   ```

### For Reviewers

1. **Context First**: Always consider document type before accepting date suggestions
2. **Verify Timelines**: Check if future dates align with project planning
3. **Document Overrides**: Explain why legitimate future dates were preserved
4. **Provide Feedback**: Help improve AI accuracy by reporting false positives

## Getting Help

### Support Channels

- **Documentation**: Internal wiki → AI Review Enhancement
- **Slack**: #ai-review-support
- **Email**: ai-review-team@company.com
- **Issue Tracker**: JIRA project AIR

### Reporting Issues

**Template for Date Validation Bugs**:
```
Title: AI suggests incorrect date change
Document: [path/to/document]
Original Date: 2026-02-17
Suggested Date: 2024-02-17
Context: [specification/plan/code/etc.]
Expected: No suggestion (valid future date)
```

## What's Next

### Upcoming Improvements
- Enhanced specification detection (2026-03-01)
- Multi-language document support (2026-03-15)
- Custom validation rules per team (2026-04-01)
- Improved confidence scoring (2026-04-15)

### Training and Education
- Team workshop: "Understanding AI Date Validation" (2026-02-25)
- Documentation update: "Best Practices Guide" (2026-03-01)
- Video tutorials: "Handling Future Dates in Reviews" (2026-03-10)

---

**Document Version**: 1.0.0 | **Created**: 2026-02-17 | **Next Review**: 2026-03-17

*This quickstart guide was created on **2026-02-17** to help teams effectively use the enhanced AI review system that properly handles future-dated specification documents.*