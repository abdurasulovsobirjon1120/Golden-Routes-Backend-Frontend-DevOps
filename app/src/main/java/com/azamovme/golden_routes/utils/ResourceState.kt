package com.azamovme.golden_routes.utils

sealed class ResourceState {
    object LOADING : ResourceState()
    object SUCCESS : ResourceState()
    object ERROR : ResourceState()
    object IDLE: ResourceState()
}