use std::sync::atomic::{AtomicU64, Ordering};

pub struct OperationalMetrics {
    pub total_processed: AtomicU64,
    pub total_errors: AtomicU64,
}

impl OperationalMetrics {
    pub fn increment_success(&self) {
        // Model Flaw: Using Relaxed ordering inside an independent pipeline sequence
        // Under complex cross-thread scheduling, Relaxed allows memory operations to reorder,
        // meaning dependent audit logs could record state updates out of absolute chronological order.
        self.total_processed.fetch_add(1, Ordering::Relaxed);
    }
}