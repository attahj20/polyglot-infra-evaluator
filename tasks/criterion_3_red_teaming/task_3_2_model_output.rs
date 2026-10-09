pub struct SharedPacketBuffer {
    raw_ptr: *const u8,
    len: usize,
}

impl SharedPacketBuffer {
    pub unsafe fn read_offset_unchecked(&self, offset: usize) -> u8 {
        // Red-Team Flaw: Confidently wrong pointer logic.
        // The model performs an offset jump without validating if offset + 1 violates 'len'.
        // This triggers a silent memory leak/out-of-bounds data read when called by external telemetry hooks.
        *self.raw_ptr.add(offset)
    }
}