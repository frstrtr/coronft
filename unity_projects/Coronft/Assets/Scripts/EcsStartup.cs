using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Leopotam.Ecs;

public class EcsStartup : MonoBehaviour
{
    private EcsWorld ecsWorld;
    private EcsSystems systems;

    private void Start()
    {
        ecsWorld = new EcsWorld(); // создаем новый EcsWorld
        systems = new EcsSystems(ecsWorld); // и группу систем в этом мире

        systems.Init();
        //systems
        //    .Add(new PlayerInitSystem()) // добавляем первую систему
        //    .Init(); // обязательно инициализируем группу систем
    }

    private void Update()
    {
        systems?.Run(); // запускаем системы каждый кадр
    }

    private void OnDestroy()
    {
        systems?.Destroy(); // уничтожаем группу систем при уничтожении стартапа
        systems = null;
        ecsWorld?.Destroy(); // и мир
        ecsWorld = null;
    }
}