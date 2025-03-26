package com.azamovme.golden_routes.presentation.screens.splash

import android.content.Intent
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.lifecycle.lifecycleScope
import androidx.navigation.fragment.findNavController
import com.azamovme.golden_routes.R
import com.azamovme.golden_routes.utils.alphaAnim
import com.azamovme.golden_routes.utils.visible
import com.azamovme.golden_routes.databinding.SplashScreenBinding
import com.azamovme.golden_routes.utils.MyAppTheme
import com.azamovme.golden_routes.utils.animationTransaction
import com.azamovme.golden_routes.utils.animationTransactionClearStack
import com.dolatkia.animatedThemeManager.AppTheme
import com.dolatkia.animatedThemeManager.ThemeFragment
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

class SplashScreen : ThemeFragment() {
    private var _binding: SplashScreenBinding? = null
    private val binding get() = _binding!!
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = SplashScreenBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        lifecycleScope.launch {
            binding.appLogo.visible()
            binding.appLogo.alphaAnim()
            delay(2000)
            findNavController().navigate(
                R.id.action_splashScreen_to_onBoardingScreen,
                null,
                animationTransactionClearStack(
                    R.id.splashScreen
                ).build()
            )
        }
    }

    override fun syncTheme(appTheme: AppTheme) {

        val myAppTheme = appTheme as MyAppTheme
        context?.let {
            binding.root.setBackgroundColor(myAppTheme.fragmentBackgroundColor(it))
            requireActivity().window.statusBarColor = myAppTheme.statusBarColor(requireContext())
            requireActivity().window.decorView.systemUiVisibility = appTheme.getStatusBarType(requireContext())
        }

    }
}