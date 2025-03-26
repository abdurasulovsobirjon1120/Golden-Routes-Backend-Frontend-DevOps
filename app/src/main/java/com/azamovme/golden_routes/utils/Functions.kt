package com.azamovme.golden_routes.utils

import android.Manifest
import android.app.Activity
import android.content.pm.PackageManager
import android.view.View
import android.view.animation.AnimationUtils
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.core.view.WindowCompat
import androidx.fragment.app.Fragment
import androidx.navigation.NavOptions
import com.azamovme.golden_routes.R

fun View.alphaAnim() {
    val anim = AnimationUtils.loadAnimation(
        this.context!!,
        R.anim.alpha_anim
    ).apply {
        duration = 1800L

        fillAfter = true
    }

    startAnimation(anim)

}

fun View.visible() {
    this.visibility = View.VISIBLE
}


fun View.gone() {
    this.visibility = View.GONE
}

private val SMS_PERMISSION_CODE = 101

fun Fragment.checkSmsPermission(): Boolean {
    return ContextCompat.checkSelfPermission(
        requireContext(),
        Manifest.permission.RECEIVE_SMS
    ) == PackageManager.PERMISSION_GRANTED
}

fun Fragment.requestSmsPermission() {
    ActivityCompat.requestPermissions(
        requireActivity(),
        arrayOf(Manifest.permission.RECEIVE_SMS, Manifest.permission.READ_SMS),
        SMS_PERMISSION_CODE
    )
}
fun initActivity(a: Activity) {
    val window = a.window
    WindowCompat.setDecorFitsSystemWindows(window, false)
//    manageThemeAndRefresh(readData<Int>("current_theme", a) ?: 0)

}

fun animationTransactionClearStack(clearFragmentID: Int): NavOptions.Builder {
    val navBuilder = NavOptions.Builder()
    navBuilder.setEnterAnim(R.anim.from_right).setExitAnim(R.anim.to_left)
        .setPopEnterAnim(R.anim.from_left).setPopExitAnim(R.anim.to_right)
        .setPopUpTo(clearFragmentID, true)
    return navBuilder
}

fun animationTransaction(): NavOptions.Builder {
    val navBuilder = NavOptions.Builder()
    navBuilder.setEnterAnim(R.anim.from_right).setExitAnim(R.anim.to_left)
        .setPopEnterAnim(R.anim.from_left).setPopExitAnim(R.anim.to_right)
    return navBuilder
}