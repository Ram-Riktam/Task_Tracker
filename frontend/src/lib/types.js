/**
 * @typedef {Object} Card
 * @property {number} id - Unique identifier for the card
 * @property {string} title - The title/content of the card
 * @property {boolean} fixed - Whether the card is fixed (non-editable/non-deletable)
 */

/**
 * @typedef {Object} Board
 * @property {Card[]} [status] - Array of cards for each status column
 */

// Export empty object to make this a module
export {};