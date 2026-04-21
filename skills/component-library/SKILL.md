---
name: component-library
description: Comprehensive React component library with 30+ production-ready components using shadcn/ui architecture, CVA variants, Radix UI primitives, and Tailwind CSS. Use when users need to (1) Create React UI components with modern patterns, (2) Build complete component systems with consistent design, (3) Implement accessible, responsive, dark-mode-ready components, (4) Generate form components with React Hook Form integration, (5) Create data display components like tables, cards, charts, or (6) Build navigation, layout, or feedback components. Provides instant generation of customizable components that would otherwise take 20-45 minutes each to hand-code.
---

# Component Library - shadcn/ui Architecture

Generate production-ready React components with shadcn/ui patterns, saving 8-10 hours per project.

## Quick Start

When generating components:
1. Create `/components/ui/` directory structure
2. Generate `lib/utils.ts` with cn() helper first
3. Create requested components with full TypeScript, variants, and accessibility
4. Include example usage for each component

## Core Setup Files

### Always generate these first:

**lib/utils.ts** - Essential cn() helper:
```typescript
import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

**components.json** - Component registry:
```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "default",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "app/globals.css",
    "baseColor": "slate",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  }
}
```

## Component Categories

### Form Components
- **Input** - Text input with variants (default, ghost, underline)
- **Select** - Custom dropdown with search, multi-select options  
- **Checkbox** - With indeterminate state support
- **Radio** - Radio groups with custom styling
- **Switch** - Toggle switches with labels
- **Textarea** - Auto-resize, character count variants
- **DatePicker** - Calendar integration, range selection
- **FileUpload** - Drag & drop, preview, progress
- **Slider** - Range input with marks, tooltips
- **Form** - React Hook Form wrapper with validation

### Display Components  
- **Card** - Container with header/footer slots
- **Table** - Sortable, filterable, pagination
- **Badge** - Status indicators with variants
- **Avatar** - Image/initials with fallback
- **Progress** - Linear and circular variants
- **Skeleton** - Loading states
- **Separator** - Visual dividers
- **ScrollArea** - Custom scrollbars

### Feedback Components
- **Alert** - Info/warning/error/success states
- **Toast** - Notifications with actions
- **Dialog/Modal** - Accessible overlays
- **Tooltip** - Hover information
- **Popover** - Positioned content
- **AlertDialog** - Confirmation dialogs

### Navigation Components
- **Navigation** - Responsive nav with mobile menu
- **Tabs** - Tab panels with keyboard nav
- **Breadcrumb** - Path navigation
- **Pagination** - Page controls
- **CommandMenu** - Command palette (⌘K)
- **ContextMenu** - Right-click menus
- **DropdownMenu** - Action menus

### Layout Components
- **Accordion** - Collapsible sections
- **Collapsible** - Show/hide content
- **ResizablePanels** - Draggable split panes
- **Sheet** - Slide-out panels
- **AspectRatio** - Maintain ratios

## Component Implementation Patterns

### Use CVA for all variants:
```typescript
import { cva, type VariantProps } from "class-variance-authority"

const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)
```

### Accessibility Requirements:
- ARIA labels and roles on all interactive elements
- Keyboard navigation (Tab, Arrow keys, Enter, Escape)
- Focus management and trapping for modals
- Screen reader announcements
- Semantic HTML elements

### Dark Mode Support:
- Use Tailwind dark: modifier
- CSS variables for theme colors
- Smooth transitions between modes

### Responsive Design:
- Mobile-first approach
- Container queries where appropriate
- Touch-friendly tap targets (min 44x44px)
- Responsive typography scale

Installation and Setup
Step 1: Initialize project using shadcn/cli v4. Choose a framework template (Next.js, Vite, TanStack Start, React Router, Astro, or Laravel) and optionally apply a preset for bundled design system configuration.

Step 2: The CLI generates a components.json configuration file. It detects the framework, configures Tailwind CSS (v3 or v4), sets up path aliases, and selects the base primitive library (Radix UI or Base UI).

Step 3: Add components individually using the add command. Use --dry-run to preview changes, --diff to see registry updates. The shadcn info command shows installed components and project configuration.

Foundation Technologies
React 19 features include Server Components support, concurrent rendering, automatic batching, and streaming SSR.

TypeScript 5.9 provides full type safety, improved inference, and enhanced developer experience.

Tailwind CSS v4 includes CSS-first configuration, CSS variables, OKLCH color support, and container queries.

Radix UI uses the unified radix-ui package with single imports. Base UI is available as an alternative primitive library.

Integration Stack includes React Hook Form for form state, Zod for schema validation, class-variance-authority for variants, Framer Motion for animations, and Lucide React for icons.

AI-Powered Architecture Design
The ShadcnUIArchitectOptimizer class uses Context7 MCP integration to design optimal shadcn/ui architectures. It initializes a Context7 client, component analyzer, and theme optimizer. The design_optimal_shadcn_architecture method takes design system requirements and fetches latest shadcn/ui and React documentation via Context7. It then optimizes component selection based on UI components and user needs, optimizes theme configuration based on brand guidelines and accessibility requirements, and returns a complete ShadcnUIArchitecture including component library, theme system, accessibility compliance, performance optimization, integration patterns, and customization strategy.

Best Practices
Requirements include using CSS variables for theme customization, implementing proper TypeScript types, following accessibility guidelines for WCAG 2.1 AA compliance, using Radix UI primitives for complex interactions, testing components with React Testing Library, optimizing bundle size with tree-shaking, and implementing responsive design patterns.

Critical Implementation Standards:

[HARD] Use CSS variables exclusively for color values. This enables dynamic theming, supports dark mode transitions, and maintains design system consistency across all components. Without CSS variables, theme changes require code modifications, dark mode fails, and brand customization becomes unmaintainable.

[HARD] Include accessibility attributes on all interactive elements. This ensures WCAG 2.1 AA compliance, screen reader compatibility, and inclusive user experience for users with disabilities. Missing accessibility attributes excludes users with disabilities, violates legal compliance requirements, and reduces application usability.

[HARD] Implement keyboard navigation for all interactive components. This provides essential navigation method for keyboard users, supports assistive technologies, and improves overall user experience efficiency. Without keyboard navigation, power users cannot efficiently use the application and accessibility compliance fails.

[SOFT] Provide loading states for asynchronous operations. This communicates operation progress to users, reduces perceived latency, and improves user confidence in application responsiveness.

[HARD] Implement error boundaries around component trees. This prevents entire application crashes from isolated component failures, enables graceful error recovery, and maintains application stability.

[HARD] Apply Tailwind CSS classes instead of inline styles. This maintains consistency with design system, enables JIT compilation benefits, supports responsive design variants, and improves bundle size optimization.

[SOFT] Implement dark mode support across all components. This provides user preference respect, reduces eye strain in low-light environments, and aligns with modern UI expectations.

Performance Optimization
Bundle Size optimization includes tree-shaking to remove unused components, code splitting for large components, lazy loading with React.lazy, and dynamic imports for heavy dependencies.

Runtime Performance optimization includes React.memo for expensive components, useMemo and useCallback for computations, virtual scrolling for large lists, and debouncing user interactions.

Accessibility includes ARIA attributes for all interactive elements, keyboard navigation support, focus management, and screen reader testing.

Advanced Patterns
Component Composition
The composable pattern involves importing Card, CardHeader, CardTitle, and CardContent from the ui/card components. A DashboardCard component accepts a title and children props, wrapping them in the Card structure with CardHeader containing CardTitle and CardContent containing the children.

Form Validation
The Zod and React Hook Form integration pattern involves importing useForm from react-hook-form, zodResolver from hookform/resolvers/zod, and z from zod. Define a formSchema with z.object containing field validations such as z.string().email() for email and z.string().min(8) for password. Infer the FormValues type from the schema. The form component uses useForm with zodResolver passing the formSchema. The form element uses form.handleSubmit with an onSubmit handler.

Works Well With
modules/cli-registry.md for CLI v4 commands, presets, RTL, migrations, and registry
shadcn-components.md module for advanced component patterns and implementation
shadcn-theming.md module for OKLCH theme system and customization strategies
moai-domain-uiux for design system architecture and principles
moai-lang-typescript for TypeScript best practices
code-frontend for frontend development patterns
Context7 Integration
Related Libraries:

shadcn/ui at /shadcn-ui/ui provides re-usable components built with Radix UI and Tailwind
Radix UI at /radix-ui/primitives provides unstyled accessible component primitives
Tailwind CSS at /tailwindlabs/tailwindcss provides utility-first CSS framework
Official Documentation:

shadcn/ui Documentation at ui.shadcn.com/docs
CLI Reference at ui.shadcn.com/docs/cli
MCP Server at ui.shadcn.com/docs/mcp
Radix UI Documentation at radix-ui.com
Tailwind CSS Documentation at tailwindcss.com
Latest Versions as of March 2026:

shadcn/cli v4
React 19
TypeScript 5.9+
Tailwind CSS v4
Unified radix-ui package


## Dependencies

Include in package.json:
```json
{
  "dependencies": {
    "@radix-ui/react-accordion": "^1.1.2",
    "@radix-ui/react-alert-dialog": "^1.0.5",
    "@radix-ui/react-avatar": "^1.0.4",
    "@radix-ui/react-checkbox": "^1.0.4",
    "@radix-ui/react-dialog": "^1.0.5",
    "@radix-ui/react-dropdown-menu": "^2.0.6",
    "@radix-ui/react-label": "^2.0.2",
    "@radix-ui/react-popover": "^1.0.7",
    "@radix-ui/react-progress": "^1.0.3",
    "@radix-ui/react-radio-group": "^1.1.3",
    "@radix-ui/react-select": "^2.0.0",
    "@radix-ui/react-separator": "^1.0.3",
    "@radix-ui/react-slider": "^1.1.2",
    "@radix-ui/react-switch": "^1.0.3",
    "@radix-ui/react-tabs": "^1.0.4",
    "@radix-ui/react-toast": "^1.1.5",
    "@radix-ui/react-tooltip": "^1.0.7",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.0.0",
    "cmdk": "^0.2.0",
    "date-fns": "^2.30.0",
    "lucide-react": "^0.263.1",
    "react-day-picker": "^8.8.0",
    "react-hook-form": "^7.45.4",
    "tailwind-merge": "^1.14.0",
    "tailwindcss-animate": "^1.0.7"
  }
}
```

## Implementation Workflow

1. **Assess Requirements**: Identify which components are needed
2. **Generate Base Files**: Create utils.ts and components.json
3. **Create Components**: Generate requested components with all features
4. **Provide Examples**: Include usage examples for each component
5. **Document Props**: Add TypeScript interfaces with JSDoc comments

## Advanced Patterns

For complex requirements, see:
- **references/form-patterns.md** - Advanced form handling
- **references/data-tables.md** - Complex table implementations  
- **references/animation-patterns.md** - Framer Motion integration
- **references/testing-setup.md** - Component testing patterns

## Performance Optimization

- Use React.memo for expensive components
- Implement virtual scrolling for long lists
- Lazy load heavy components
- Optimize bundle size with tree shaking
- Use CSS containment for layout stability

## Component Generation Tips

When generating components:
- Include all variant combinations
- Add proper TypeScript types
- Implement keyboard shortcuts
- Include loading and error states
- Provide Storybook stories structure
- Add comprehensive prop documentation
- Include accessibility attributes
- Test with screen readers
