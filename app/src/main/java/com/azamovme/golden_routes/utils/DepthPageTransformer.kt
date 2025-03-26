package com.azamovme.golden_routes.utils

import android.view.View
import androidx.viewpager.widget.ViewPager
import androidx.viewpager2.widget.ViewPager2
import kotlin.math.abs

class DepthPageTransformer : ViewPager.PageTransformer {
    override fun transformPage(view: View, position: Float) {
        when {
            position < -1 -> {
                view.alpha = 0f
            }

            position <= 0 -> {
                view.alpha = 1f
                view.translationX = 0f
                view.scaleX = 1f
                view.scaleY = 1f
            }

            position <= 1 -> {
                view.alpha = 1 - position
                view.translationX = view.width * -position
                val scaleFactor = 0.75f + (1 - 0.75f) * (1 - abs(position))
                view.scaleX = scaleFactor
                view.scaleY = scaleFactor
            }

            else -> {
                view.alpha = 0f
            }
        }
    }
}
