# 🧩 Tailwind CSS Cheatsheet:

This cheatsheet gives each class a **plain-English meaning** so you understand what it _does_, not just how to type it.

---

## 🎯 Flexbox Essentials

| Class                                                  | Meaning                                         |
| ------------------------------------------------------ | ----------------------------------------------- |
| `flex`                                                 | Lay children in a **row** (default direction)   |
| `flex-col`                                             | Stack children **vertically**                   |
| `justify-start` / `justify-center` / `justify-between` | Control **spacing along main axis**             |
| `items-start` / `items-center` / `items-end`           | Control **alignment across cross axis**         |
| `mt-auto`                                              | Push element **down** to the bottom in a column |
| `flex-grow` / `flex-1`                                 | Take up **remaining space** in container        |

---

## 📏 Sizing & Spacing

| Class                      | Meaning                                 |
| -------------------------- | --------------------------------------- |
| `w-32` / `h-32`            | Width/Height = 32 × 0.25rem (i.e. 8rem) |
| `w-full` / `h-full`        | Fill 100% of parent width/height        |
| `min-h-*` / `max-w-*`      | Minimum or maximum size                 |
| `p-4` / `px-2` / `py-1`    | Padding (inner space)                   |
| `m-4` / `mt-2` / `mx-auto` | Margin (outer space)                    |

---

## 🧭 Positioning & Layout

| Class               | Meaning                                                  |
| ------------------- | -------------------------------------------------------- |
| `relative`          | Allow child with `absolute` to position itself from this |
| `absolute`          | Position relative to nearest `relative` parent           |
| `top-0` / `right-0` | Pin to top/right                                         |
| `sticky top-0`      | Stick to top of page when scrolling                      |
| `z-10` / `z-50`     | Control stack order (what's in front)                    |

---

## 🔠 Text & Overflow

| Class                  | Meaning                                  |
| ---------------------- | ---------------------------------------- |
| `text-sm` / `text-2xl` | Font size                                |
| `font-bold`            | Make text bold                           |
| `truncate`             | One line text with ellipsis (`...`)      |
| `line-clamp-3`         | Max 3 lines of text, then ellipsis       |
| `overflow-auto`        | Add scrollbars **if needed**             |
| `overflow-scroll`      | Always scrollable                        |
| `overflow-clip`        | Hide overflow with no scroll or ellipsis |

---

## 🎨 Background, Border, Shadow

| Class                                | Meaning                        |
| ------------------------------------ | ------------------------------ |
| `bg-white` / `bg-gray-800`           | Background color               |
| `border` / `border-gray-300`         | Add border with optional color |
| `rounded` / `rounded-lg`             | Round the corners              |
| `shadow` / `shadow-md` / `shadow-lg` | Add drop shadow effect         |

---

## 🌗 Dark Mode

| Class              | Meaning                         |
| ------------------ | ------------------------------- |
| `dark:bg-gray-800` | Background only in dark mode    |
| `dark:text-white`  | Text becomes white in dark mode |

---

## 🎛️ Display & Visibility

| Class          | Meaning                                 |
| -------------- | --------------------------------------- |
| `hidden`       | Do not render                           |
| `block`        | Block-level element                     |
| `inline-block` | Inline element that behaves like block  |
| `sr-only`      | Screen reader only (invisible to users) |

---

## 🧩 Misc Utilities

| Class               | Meaning                                      |
| ------------------- | -------------------------------------------- |
| `cursor-pointer`    | Show hand on hover                           |
| `transition`        | Enable smooth animation                      |
| `hover:bg-blue-800` | Change background on hover                   |
| `focus:ring-4`      | Show focus outline (great for accessibility) |

---

## 📚 Tailwind Best Learning Strategy

1. Use the [Tailwind Docs](https://tailwindcss.com/docs)
2. Install [VSCode IntelliSense plugin](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)
3. Practice with [Tailwind Play](https://play.tailwindcss.com)
