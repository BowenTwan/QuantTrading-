from cpython.object cimport PyObject
from numpy cimport (
    float32_t,
    float64_t,
    int8_t,
    int16_t,
    int32_t,
    int64_t,
    uint8_t,
    uint16_t,
    uint32_t,
    uint64_t,
)


cdef extern from "khash_python.h":
    const int KHASH_TRACE_DOMAIN

    ctypedef uint32_t khint_t
    ctypedef khint_t khiter_t

    ctypedef struct kh_pymap_t:
        khint_t n_buckets, size, n_occupied, upper_bound
        uint32_t *flags
        PyObject **keys
        size_t *vals

    kh_pymap_t* kh_init_pymap()
    void kh_destroy_pymap(kh_pymap_t*)
    void kh_clear_pymap(kh_pymap_t*)
    khint_t kh_get_pymap(kh_pymap_t*, PyObject*)
    void kh_resize_pymap(kh_pymap_t*, khint_t)
    khint_t kh_put_pymap(kh_pymap_t*, PyObject*, int*)
    void kh_del_pymap(kh_pymap_t*, khint_t)

    bint kh_exist_pymap(kh_pymap_t*, khiter_t)

    ctypedef struct kh_pyset_t:
        khint_t n_buckets, size, n_occupied, upper_bound
        uint32_t *flags
        PyObject **keys
        size_t *vals

    kh_pyset_t* kh_init_pyset()
    void kh_destroy_pyset(kh_pyset_t*)
    void kh_clear_pyset(kh_pyset_t*)
    khint_t kh_get_pyset(kh_pyset_t*, PyObject*)
    void kh_resize_pyset(kh_pyset_t*, khint_t)
    khint_t kh_put_pyset(kh_pyset_t*, PyObject*, int*)
    void kh_del_pyset(kh_pyset_t*, khint_t)

    bint kh_exist_pyset(kh_pyset_t*, khiter_t)

    ctypedef char* kh_cstr_t

    ctypedef struct kh_str_t:
        khint_t n_buckets, size, n_occupied, upper_bound
        uint32_t *flags
        kh_cstr_t *keys
        size_t *vals

    kh_str_t* kh_init_str() nogil
    void kh_destroy_str(kh_str_t*) nogil
    void kh_clear_str(kh_str_t*) nogil
    khint_t kh_get_str(kh_str_t*, kh_cstr_t) nogil
    void kh_resize_str(kh_str_t*, khint_t) nogil
    khint_t kh_put_str(kh_str_t*, kh_cstr_t, int*) nogil
    void kh_del_str(kh_str_t*, khint_t) nogil

    bint kh_exist_str(kh_str_t*, khiter_t) nogil

    ctypedef struct kh_str_starts_t:
        kh_str_t *table
        int starts[256]

    kh_str_starts_t* kh_init_str_starts() nogil
    khint_t kh_put_str_starts_item(kh_str_starts_t* table, char* key,
                                   int* ret) nogil
    khint_t kh_get_str_starts_item(kh_str_starts_t* table, char* key) nogil
    void kh_destroy_str_starts(kh_str_starts_t*) nogil
    void kh_resize_str_starts(kh_str_starts_t*, khint_t) nogil

    # sweep factorize

    ctypedef struct kh_strbox_t:
        khint_t n_buckets, size, n_occupied, upper_bound
        uint32_t *flags
        kh_cstr_t *keys
        PyObject **vals

    kh_strbox_t* kh_init_strbox() nogil
    void kh_destroy_strbox(kh_strbox_t*) nogil
    void kh_clear_strbox(kh_strbox_t*) nogil
    khint_t kh_get_strbox(kh_strbox_t*, kh_cstr_t) nogil
    void kh_resize_strbox(kh_strbox_t*, khint_t) nogil
    khint_t kh_put_strbox(kh_strbox_t*, kh_cstr_t, int*) nogil
    void kh_del_strbox(kh_strbox_t*, khint_t) nogil

    bint kh_exist_strbox(kh_strbox_t*, khiter_t) nogil

include "khash_for_primitive_helper.pxi"
