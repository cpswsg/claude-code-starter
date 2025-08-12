# React + TypeScript Project

## Project Overview

This is a modern React application built with TypeScript, focusing on type safety, developer experience, and maintainable component architecture.

**Project Type**: Web Application (Frontend)
**Primary Language**: TypeScript
**Framework/Stack**: React 18 + Vite + TypeScript

## Development Guidelines

### Code Style & Conventions

- Use **PascalCase** for React components and type definitions
- Use **camelCase** for functions, variables, and props
- Use **kebab-case** for file names and CSS classes
- Prefer functional components with hooks over class components
- Use TypeScript strict mode - no `any` types allowed
- Use named exports for components, default exports for pages
- Co-locate component styles (CSS modules or styled-components)

### Component Architecture

- Follow the **component composition pattern**
- Create reusable UI components in `src/components/`
- Keep business logic in custom hooks (`src/hooks/`)
- Use React Query for server state management
- Use Zustand or Context API for client state management
- Implement proper prop typing with TypeScript interfaces

### File Structure

```
src/
├── components/          # Reusable UI components
│   ├── ui/             # Base UI components (Button, Input, etc.)
│   └── layout/         # Layout components (Header, Sidebar, etc.)
├── pages/              # Page-level components (routes)
├── hooks/              # Custom React hooks
├── services/           # API calls and external services
├── utils/              # Helper functions and utilities
├── types/              # TypeScript type definitions
├── stores/             # State management (Zustand stores)
└── styles/             # Global styles and CSS modules
```

## Testing Strategy

- **Testing Framework**: Vitest + React Testing Library
- **Coverage Requirements**: Maintain 80%+ coverage for components and hooks
- **Test Types**: Unit tests for components, integration tests for user flows
- Write tests alongside components - prefer `.test.tsx` files next to components
- Test behavior, not implementation details
- Use MSW (Mock Service Worker) for API mocking in tests

### Testing Patterns

```typescript
// Component testing example
import { render, screen, userEvent } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import { Button } from './Button'

describe('Button', () => {
  it('calls onClick when clicked', async () => {
    const handleClick = vi.fn()
    render(<Button onClick={handleClick}>Click me</Button>)
    
    await userEvent.click(screen.getByRole('button'))
    expect(handleClick).toHaveBeenCalledOnce()
  })
})
```

## Dependencies & Package Management

- Use **npm** for package management (lock file: package-lock.json)
- Pin exact versions for production dependencies
- Use `npm ci` in production/CI environments
- Keep dependencies up to date with regular audits (`npm audit`)
- Prefer packages with TypeScript support built-in
- Minimize bundle size - use tree-shaking friendly packages

### Key Dependencies

- **React 18**: Main framework with concurrent features
- **TypeScript**: Type safety and developer experience
- **Vite**: Fast build tool and development server
- **React Router**: Client-side routing
- **React Query**: Server state management and caching
- **Zustand**: Lightweight state management
- **React Hook Form**: Form handling with validation

## Performance Requirements

- **Initial Load**: < 2 seconds on 3G connection
- **Core Web Vitals**: LCP < 2.5s, FID < 100ms, CLS < 0.1
- **Bundle Size**: Keep main bundle < 200KB gzipped
- Implement code splitting for routes and heavy components
- Use React.memo() and useMemo() for expensive operations
- Optimize images with modern formats (WebP, AVIF)
- Implement proper loading states and error boundaries

## Build & Development

### Development Server
```bash
npm run dev          # Start development server (http://localhost:5173)
npm run dev:host     # Expose dev server to network
```

### Building & Testing
```bash
npm run build        # Production build
npm run preview      # Preview production build locally
npm run test         # Run test suite
npm run test:watch   # Run tests in watch mode
npm run test:ui      # Run tests with UI
npm run coverage     # Generate coverage report
```

### Code Quality
```bash
npm run lint         # ESLint checking
npm run lint:fix     # Fix auto-fixable ESLint issues
npm run type-check   # TypeScript compilation check
npm run format       # Prettier formatting
```

## API Integration

- Use **React Query** for all server communications
- Implement proper error handling with error boundaries
- Use TypeScript interfaces for API response types
- Configure base URLs and auth headers in a service layer
- Implement request/response interceptors for common functionality

### API Patterns

```typescript
// API service example
import { useQuery, useMutation } from '@tanstack/react-query'

export const useUsers = () => {
  return useQuery({
    queryKey: ['users'],
    queryFn: () => api.get<User[]>('/users').then(res => res.data)
  })
}

export const useCreateUser = () => {
  return useMutation({
    mutationFn: (user: CreateUserData) => api.post('/users', user),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['users'] })
    }
  })
}
```

## Security Considerations

- Sanitize all user inputs before rendering
- Use HTTPS for all API communications
- Implement proper authentication token handling
- Never store sensitive data in localStorage
- Use Content Security Policy headers
- Validate all form inputs on both client and server
- Implement proper CORS configuration

## Deployment & Environment

- **Development**: Local development with Vite dev server
- **Production**: Static build deployed to CDN/hosting service
- Use environment variables for configuration (VITE_* prefix)
- Implement proper error tracking (Sentry, LogRocket)
- Set up monitoring for Core Web Vitals and user experience

### Environment Variables

```bash
# .env.example
VITE_API_BASE_URL=https://api.example.com
VITE_APP_NAME=My React App
VITE_ENVIRONMENT=development
```

## Common Commands

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run test` - Run test suite
- `npm run lint` - Check code quality
- `npm run type-check` - Verify TypeScript compilation
- `npm run preview` - Preview production build
- `npm audit` - Check for security vulnerabilities

## Important Notes

- This project uses React 18 with concurrent features enabled
- TypeScript strict mode is enabled - handle all type errors
- All components should be properly typed with interfaces
- Use React DevTools and React Query DevTools for debugging
- Performance is critical - monitor bundle size and Core Web Vitals
- Follow accessibility best practices (semantic HTML, ARIA labels)

## External Resources

- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Vite Documentation](https://vitejs.dev/)
- [React Query Documentation](https://tanstack.com/query/)
- [Testing Library Documentation](https://testing-library.com/)