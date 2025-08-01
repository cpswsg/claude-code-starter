# Comprehensive UI Healing System

## Step 1: Initial Assessment & Documentation

Take a screenshot of the target screen/component using the playwright MCP, then document:

- **Context**: What is this interface trying to accomplish?
- **Target users**: Who is the primary audience?
- **Device/platform**: Desktop, mobile, tablet, or responsive?
- **Accessibility requirements**: Any specific compliance needs (WCAG, etc.)?

## Step 2: Multi-Dimensional Evaluation

Grade the interface across these specific criteria (1-10 scale each):

### Visual Design (Weight: 20%)

- **Typography**: Readability, hierarchy, consistency
- **Color & Contrast**: Accessibility compliance, brand alignment
- **Layout & Spacing**: Balance, white space usage, visual hierarchy
- **Brand Consistency**: Alignment with design system/guidelines

### User Experience (Weight: 30%)

- **Navigation**: Intuitive pathways, clear information architecture
- **Content Clarity**: Language, messaging, information hierarchy
- **User Flow**: Logical progression, minimal friction
- **Error Prevention**: Clear feedback, validation, recovery paths

### Accessibility (Weight: 25%)

- **Screen Reader**: Proper ARIA labels, semantic HTML
- **Keyboard Navigation**: Tab order, focus indicators
- **Color Dependency**: Information not reliant on color alone
- **Text Scaling**: Readable at 200% zoom

### Technical Performance (Weight: 15%)

- **Loading Speed**: Visual elements, interactive responsiveness
- **Responsive Design**: Cross-device compatibility
- **Interactive Elements**: Button states, hover effects, touch targets

### Content Strategy (Weight: 10%)

- **Relevance**: Information matches user needs
- **Scannability**: Easy to parse and digest
- **Actionability**: Clear next steps for users

**Overall Score Calculation**: Weighted average of all categories
**Pass Threshold**: 9.0/10 overall with no individual category below 8.0

## Step 3: Detailed Analysis & Action Planning

For any interface scoring below threshold, think harder:

### Issue Documentation

- **Specific problems identified** (with screenshot annotations)
- **Impact assessment** (user experience, accessibility, business goals)
- **Priority ranking** (critical, important, nice-to-have)

### Solution Strategy

- **Proposed changes** with rationale
- **Implementation approach** (quick fixes vs. major redesigns)
- **Success metrics** (how will improvement be measured?)
- **Potential risks** or unintended consequences

## Step 4: Implementation & Validation

- **Apply highest-priority changes** first
- **Take new screenshot** for comparison
- **Re-evaluate using Step 2 criteria**
- **Document improvements made** and lessons learned

## Step 5: Iterative Refinement

- **A/B test considerations** (if applicable)
- **User feedback integration** opportunities
- **Long-term monitoring** plan
- **Knowledge capture** for future similar interfaces

## Success Criteria

- **Minimum 9.0/10 overall score**
- **No category below 8.0/10**
- **Measurable improvement** in key user metrics
- **Accessibility compliance** verified
- **Stakeholder approval** obtained

## Documentation Requirements

Maintain a healing log including:

- Before/after screenshots
- Score progressions
- Changes implemented
- Rationale for decisions
- Lessons learned for future applications

You **MUST** save the log files in `docs/ai/uix/` folder.

**You MUST save the log files in `docs/ai/uix/` folder.**
